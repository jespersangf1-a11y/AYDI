"""Tests for retry framework and circuit breaker."""

import asyncio
import pytest
import time
from unittest.mock import AsyncMock

from app.core.retry import (
    CircuitBreaker,
    CircuitState,
    NonRetryableError,
    RetryableError,
    RetryResult,
    retry_async,
)


class TestRetryAsync:
    @pytest.mark.asyncio
    async def test_success_first_try(self):
        func = AsyncMock(return_value="ok")
        result = await retry_async(func, context="test")
        assert result.success is True
        assert result.value == "ok"
        assert result.attempts == 1
        assert func.call_count == 1

    @pytest.mark.asyncio
    async def test_success_after_retry(self):
        func = AsyncMock(side_effect=[ConnectionError("fail"), "ok"])
        result = await retry_async(
            func, max_retries=2, base_delay=0.01, context="test"
        )
        assert result.success is True
        assert result.value == "ok"
        assert result.attempts == 2
        assert func.call_count == 2

    @pytest.mark.asyncio
    async def test_all_retries_exhausted(self):
        func = AsyncMock(side_effect=ConnectionError("fail"))
        result = await retry_async(
            func, max_retries=2, base_delay=0.01, context="test"
        )
        assert result.success is False
        assert isinstance(result.error, ConnectionError)
        assert result.attempts == 3  # initial + 2 retries

    @pytest.mark.asyncio
    async def test_no_retries(self):
        func = AsyncMock(side_effect=ConnectionError("fail"))
        result = await retry_async(func, max_retries=0, context="test")
        assert result.success is False
        assert result.attempts == 1

    @pytest.mark.asyncio
    async def test_non_retryable_error_stops_immediately(self):
        func = AsyncMock(side_effect=NonRetryableError("bad input"))
        result = await retry_async(
            func, max_retries=5, base_delay=0.01, context="test"
        )
        assert result.success is False
        assert result.attempts == 1
        assert isinstance(result.error, NonRetryableError)

    @pytest.mark.asyncio
    async def test_non_retryable_exception_stops(self):
        """Exceptions not in retryable_exceptions stop retries."""
        func = AsyncMock(side_effect=ValueError("bad"))
        result = await retry_async(
            func, max_retries=3, base_delay=0.01, context="test"
        )
        assert result.success is False
        assert result.attempts == 1  # No retry for ValueError

    @pytest.mark.asyncio
    async def test_timeout_triggers_retry(self):
        call_count = 0

        async def slow_then_fast():
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                await asyncio.sleep(10)  # Will timeout
            return "ok"

        result = await retry_async(
            slow_then_fast,
            max_retries=2,
            base_delay=0.01,
            timeout=0.05,
            context="test",
        )
        assert result.success is True
        assert result.value == "ok"
        assert result.attempts == 2

    @pytest.mark.asyncio
    async def test_retryable_error_marker(self):
        func = AsyncMock(side_effect=[RetryableError("temp"), "ok"])
        result = await retry_async(
            func, max_retries=2, base_delay=0.01, context="test"
        )
        assert result.success is True
        assert result.attempts == 2

    @pytest.mark.asyncio
    async def test_on_retry_callback(self):
        attempts = []

        def on_retry(attempt, exc):
            attempts.append(attempt)

        func = AsyncMock(side_effect=[ConnectionError(), ConnectionError(), "ok"])
        result = await retry_async(
            func,
            max_retries=3,
            base_delay=0.01,
            on_retry=on_retry,
            context="test",
        )
        assert result.success is True
        assert attempts == [1, 2]

    @pytest.mark.asyncio
    async def test_kwargs_passed(self):
        async def func(a, b=None):
            return f"{a}-{b}"

        result = await retry_async(
            func, args=("hello",), kwargs={"b": "world"}, context="test"
        )
        assert result.success is True
        assert result.value == "hello-world"

    @pytest.mark.asyncio
    async def test_total_time_tracked(self):
        func = AsyncMock(return_value="ok")
        result = await retry_async(func, context="test")
        assert result.total_time_ms >= 0


class TestCircuitBreaker:
    def test_starts_closed(self):
        cb = CircuitBreaker("test", failure_threshold=3)
        assert cb.state == CircuitState.CLOSED
        assert cb.is_closed is True
        assert cb.is_open is False

    def test_opens_after_threshold(self):
        cb = CircuitBreaker("test", failure_threshold=3)
        cb.record_failure()
        cb.record_failure()
        assert cb.is_open is False
        cb.record_failure()  # 3rd failure -> threshold
        assert cb.is_open is True

    def test_success_resets_failure_count(self):
        cb = CircuitBreaker("test", failure_threshold=3)
        cb.record_failure()
        cb.record_failure()
        cb.record_success()  # Reset
        cb.record_failure()  # 1st after reset
        assert cb.is_open is False

    def test_recovers_after_timeout(self):
        cb = CircuitBreaker("test", failure_threshold=2, recovery_timeout=0.05)
        cb.record_failure()
        cb.record_failure()
        assert cb.is_open is True

        # Wait for recovery
        time.sleep(0.06)
        assert cb.state == CircuitState.HALF_OPEN

    def test_half_open_success_closes(self):
        cb = CircuitBreaker("test", failure_threshold=2, recovery_timeout=0.01)
        cb.record_failure()
        cb.record_failure()
        time.sleep(0.02)
        assert cb.state == CircuitState.HALF_OPEN

        cb.record_success()
        assert cb.state == CircuitState.CLOSED

    def test_half_open_failure_reopens(self):
        cb = CircuitBreaker("test", failure_threshold=2, recovery_timeout=0.01)
        cb.record_failure()
        cb.record_failure()
        time.sleep(0.02)
        assert cb.state == CircuitState.HALF_OPEN

        cb.record_failure()
        assert cb.state == CircuitState.OPEN

    def test_manual_reset(self):
        cb = CircuitBreaker("test", failure_threshold=2)
        cb.record_failure()
        cb.record_failure()
        assert cb.is_open is True

        cb.reset()
        assert cb.is_closed is True

    def test_get_status(self):
        cb = CircuitBreaker("api_test", failure_threshold=5)
        cb.record_failure()
        status = cb.get_status()
        assert status["name"] == "api_test"
        assert status["state"] == "closed"
        assert status["failure_count"] == 1
        assert status["failure_threshold"] == 5
