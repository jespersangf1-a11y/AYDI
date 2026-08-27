"""JWT authentication utilities."""
from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from passlib.context import CryptContext

from app.core.config import settings

# Read secrets from settings (environment variable or .env file)
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES
REFRESH_TOKEN_EXPIRE_DAYS = settings.REFRESH_TOKEN_EXPIRE_DAYS

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# A real bcrypt hash of a value nobody can supply. Verifying against it costs
# the same as verifying a genuine password, which is the point.
_DUMMY_HASH = pwd_context.hash("aydi-dummy-password-for-constant-time-login")


def waste_password_time() -> None:
    """Burn the same time a real password check would take.

    Login answered an unknown e-mail in ~270 ms and a known one in ~836 ms,
    because only the known one reached bcrypt. That difference is a reliable
    oracle for enumerating which addresses have an account. Running the hash
    against a dummy value removes it.
    """
    pwd_context.verify("aydi-dummy-password-for-constant-time-login-x", _DUMMY_HASH)


# ---------------------------------------------------------------------------
# Password policy
# ---------------------------------------------------------------------------

MIN_PASSWORD_LENGTH = 10

#: Passwords seen constantly in credential-stuffing lists. Length alone would
#: have accepted every one of these.
_FORBIDDEN_PASSWORDS = {
    "passwort", "password", "password1", "passwort1", "12345678", "123456789",
    "1234567890", "qwertzuiop", "qwertyuiop", "iloveyou", "admin123",
    "administrator", "willkommen", "welcome1", "sonnenschein", "letmein",
    "aydi1234", "aydi12345", "demo1234", "changeme", "geheim123",
}


def validate_password_strength(password: str, *, email: str | None = None) -> None:
    """Raise ``ValueError`` with a German message if the password is too weak.

    The rule used to be "at least 8 characters" and nothing else, so
    ``12345678`` was accepted.
    """
    if len(password) < MIN_PASSWORD_LENGTH:
        raise ValueError(
            f"Das Passwort muss mindestens {MIN_PASSWORD_LENGTH} Zeichen lang sein."
        )

    lowered = password.lower()
    if lowered in _FORBIDDEN_PASSWORDS:
        raise ValueError("Dieses Passwort ist zu gebräuchlich. Bitte ein anderes wählen.")

    categories = sum(
        (
            any(c.islower() for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            any(not c.isalnum() for c in password),
        )
    )
    if categories < 3:
        raise ValueError(
            "Das Passwort muss mindestens drei der vier Zeichenarten enthalten: "
            "Kleinbuchstaben, Großbuchstaben, Ziffern, Sonderzeichen."
        )

    if len(set(password)) < 5:
        raise ValueError("Das Passwort enthält zu wenige verschiedene Zeichen.")

    if email:
        local_part = email.split("@")[0].lower()
        if len(local_part) >= 4 and local_part in lowered:
            raise ValueError("Das Passwort darf nicht die eigene E-Mail-Adresse enthalten.")


def create_access_token(user_id: str, role: str, expires_delta: Optional[timedelta] = None) -> str:
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    payload = {
        "sub": user_id,
        "role": role,
        "type": "access",
        "exp": expire,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(user_id: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {
        "sub": user_id,
        "type": "refresh",
        "exp": expire,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    """Decode and validate a JWT token. Raises jwt.PyJWTError on failure."""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
