"""Retry framework with exponential backoff for external service calls.

Provides resilient wrappers for:
- AI API calls (Anthropic Claude)
- Forum scraping
- Manufacturer database lookups
- Any external HTTP call

Usage:
    from app.core.retry import retry_async, CircuitBreaker

    # Simple retry
    result = await retry_async(
        func=call_anthropic_api,
        args=(prompt, image_data),
        max_retries=3,
        base_delay=1.0,
        timeout=30.0,
    )

    # Circuit breaker for repeated failures
    breaker = CircuitBreaker("anthropic_api", failure_threshold=5)
    if breaker.is_open:
        return fallback_result()
    try:
        result = await call_api()
        breaker.record_success()
    except Exception as e:
        breaker.record_failure()
        raise
"""

from __future__ import annotations

import asyncio
import logging
import random
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Awaitable, Callable, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


# ---------------------------------------------------------------------------
# Retryable exceptions
# ---------------------------------------------------------------------------

class RetryableError(Exception):
    """Marker for errors that should be retried."""
    pass


class NonRetryableError(Exception):
    """Marker for errors that should NOT be retried."""
    pass


# Default retryable exception types
RETRYABLE_EXCEPTIONS: tuple[type[Exception], ...] = (
    TimeoutError,
    asyncio.TimeoutError,
    ConnectionError,
    ConnectionResetError,
    ConnectionRefusedError,
    OSError,
    RetryableError,
)


# ---------------------------------------------------------------------------
# Retry with exponential backoff
# ---------------------------------------------------------------------------

@dataclass
class RetryResult:
    """Result of a retry operation."""
    success: bool
    value: Any = None
    error: Exception | None = None
    attempts: int = 0
    total_time_ms: float = 0.0


async def retry_async(
    func: Callable[..., Awaitable[T]],
    args: tuple = (),
    kwargs: dict | None = None,
    *,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 30.0,
    backoff_factor: float = 2.0,
    jitter: bool = True,
    timeout: float | None = None,
    retryable_exceptions: tuple[type[Exception], ...] = RETRYABLE_EXCEPTIONS,
    on_retry: Callable[[int, Exception], None] | None = None,
    context: str = "",
) -> RetryResult:
    """Execute an async function with exponential backoff retry.

    Args:
        func: Async function to call.
        args: Positional arguments for func.
        kwargs: Keyword arguments for func.
        max_retries: Maximum number of retry attempts (0 = no retries).
        base_delay: Initial delay between retries in seconds.
        max_delay: Maximum delay between retries.
        backoff_factor: Multiplier for delay after each retry.
        jitter: Add random jitter to prevent thundering herd.
        timeout: Per-attempt timeout in seconds (None = no timeout).
        retryable_exceptions: Tuple of exception types to retry on.
        on_retry: Optional callback(attempt_number, exception) called before retry.
        context: Description for logging.

    Returns:
        RetryResult with success status, value, and metadata.
    """
    if kwargs is None:
        kwargs = {}

    start_time = time.monotonic()
    last_error: Exception | None = None

    for attempt in range(max_retries + 1):
        try:
            if timeout is not None:
                value = await asyncio.wait_for(
                    func(*args, **kwargs),
                    timeout=timeout,
                )
            else:
                value = await func(*args, **kwargs)

            elapsed = (time.monotonic() - start_time) * 1000
            if attempt > 0:
                logger.info(
                    "%s: succeeded on attempt %d/%d (%.0fms total)",
                    context or func.__name__, attempt + 1, max_retries + 1, elapsed,
                )
            return RetryResult(
                success=True,
                value=value,
                attempts=attempt + 1,
                total_time_ms=elapsed,
            )

        except NonRetryableError as e:
            # Don't retry these
            elapsed = (time.monotonic() - start_time) * 1000
            logger.warning("%s: non-retryable error: %s", context or func.__name__, e)
            return RetryResult(
                success=False,
                error=e,
                attempts=attempt + 1,
                total_time_ms=elapsed,
            )

        except retryable_exceptions as e:
            last_error = e

            if attempt >= max_retries:
                break  # No more retries

            # Calculate delay with exponential backoff
            delay = min(base_delay * (backoff_factor ** attempt), max_delay)
            if jitter:
                delay = delay * (0.5 + random.random() * 0.5)

            logger.warning(
                "%s: attempt %d/%d failed (%s: %s), retrying in %.1fs",
                context or func.__name__, attempt + 1, max_retries + 1,
                type(e).__name__, str(e)[:200], delay,
            )

            if on_retry:
                on_retry(attempt + 1, e)

            await asyncio.sleep(delay)

        except Exception as e:
            # Non-retryable exception
            elapsed = (time.monotonic() - start_time) * 1000
            logger.error(
                "%s: non-retryable error on attempt %d: %s",
                context or func.__name__, attempt + 1, e,
            )
            return RetryResult(
                success=False,
                error=e,
                attempts=attempt + 1,
                total_time_ms=elapsed,
            )

    # All retries exhausted
    elapsed = (time.monotonic() - start_time) * 1000
    logger.error(
        "%s: all %d attempts failed (%.0fms total). Last error: %s",
        context or func.__name__, max_retries + 1, elapsed, last_error,
    )
    return RetryResult(
        success=False,
        error=last_error,
        attempts=max_retries + 1,
        total_time_ms=elapsed,
    )


# ---------------------------------------------------------------------------
# Circuit Breaker
# ---------------------------------------------------------------------------

class CircuitState(str, Enum):
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing, reject calls
    HALF_OPEN = "half_open"  # Testing if service recovered


@dataclass
class CircuitBreaker:
    """Circuit breaker for external services.

    Prevents cascade failures by stopping calls to a failing service.
    After a cooldown period, allows a test call through (half-open).

    Usage:
        breaker = CircuitBreaker("anthropic_api")
        if breaker.is_open:
            return fallback_result()
        try:
            result = await call_api()
            breaker.record_success()
        except Exception:
            breaker.record_failure()
    """
    name: str
    failure_threshold: int = 5
    recovery_timeout: float = 60.0  # seconds
    half_open_max_calls: int = 1

    # Internal state
    _state: CircuitState = field(default=CircuitState.CLOSED, init=False)
    _failure_count: int = field(default=0, init=False)
    _success_count: int = field(default=0, init=False)
    _last_failure_time: float = field(default=0.0, init=False)
    _half_open_calls: int = field(default=0, init=False)

    @property
    def state(self) -> CircuitState:
        if self._state == CircuitState.OPEN:
            # Check if recovery timeout has passed
            if time.monotonic() - self._last_failure_time >= self.recovery_timeout:
                self._state = CircuitState.HALF_OPEN
                self._half_open_calls = 0
                logger.info("Circuit %s: OPEN -> HALF_OPEN", self.name)
        return self._state

    @property
    def is_open(self) -> bool:
        return self.state == CircuitState.OPEN

    @property
    def is_closed(self) -> bool:
        return self.state == CircuitState.CLOSED

    def allow_request(self) -> bool:
        """Whether a call may proceed right now.

        CLOSED -> always. OPEN -> never. HALF_OPEN -> admit at most
        ``half_open_max_calls`` probe(s); further calls are rejected until the
        probe resolves (record_success/record_failure), so a recovering
        downstream service is not hit by a thundering herd.
        """
        st = self.state  # may transition OPEN -> HALF_OPEN when the timeout elapsed
        if st == CircuitState.OPEN:
            return False
        if st == CircuitState.HALF_OPEN:
            if self._half_open_calls >= self.half_open_max_calls:
                return False
            self._half_open_calls += 1
            return True
        return True

    def record_success(self) -> None:
        """Record a successful call."""
        if self._state == CircuitState.HALF_OPEN:
            self._success_count += 1
            if self._success_count >= self.half_open_max_calls:
                self._state = CircuitState.CLOSED
                self._failure_count = 0
                self._success_count = 0
                logger.info("Circuit %s: HALF_OPEN -> CLOSED (recovered)", self.name)
        else:
            self._failure_count = 0

    def record_failure(self) -> None:
        """Record a failed call."""
        self._failure_count += 1
        self._last_failure_time = time.monotonic()

        if self._state == CircuitState.HALF_OPEN:
            self._state = CircuitState.OPEN
            logger.warning("Circuit %s: HALF_OPEN -> OPEN (still failing)", self.name)
        elif self._failure_count >= self.failure_threshold:
            self._state = CircuitState.OPEN
            logger.warning(
                "Circuit %s: CLOSED -> OPEN (threshold %d reached)",
                self.name, self.failure_threshold,
            )

    def reset(self) -> None:
        """Manually reset the circuit breaker."""
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._success_count = 0
        self._half_open_calls = 0

    def get_status(self) -> dict:
        """Get current circuit breaker status for monitoring."""
        return {
            "name": self.name,
            "state": self.state.value,
            "failure_count": self._failure_count,
            "failure_threshold": self.failure_threshold,
            "recovery_timeout": self.recovery_timeout,
        }


# ---------------------------------------------------------------------------
# Pre-configured circuit breakers for AYDI services
# ---------------------------------------------------------------------------

_breakers: dict[str, CircuitBreaker] = {}


def get_circuit_breaker(
    name: str,
    failure_threshold: int = 5,
    recovery_timeout: float = 60.0,
) -> CircuitBreaker:
    """Get or create a named circuit breaker (singleton per name)."""
    if name not in _breakers:
        _breakers[name] = CircuitBreaker(
            name=name,
            failure_threshold=failure_threshold,
            recovery_timeout=recovery_timeout,
        )
    return _breakers[name]


def get_all_circuit_status() -> list[dict]:
    """Get status of all circuit breakers (for monitoring endpoint)."""
    return [b.get_status() for b in _breakers.values()]
