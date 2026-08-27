#!/bin/sh
# AYDI backend entrypoint.
#
# Runs Alembic migrations to head (idempotent), then execs uvicorn.
# Aborts the container start if migrations fail — that's the right
# behavior in production: never serve traffic against an unknown schema.
set -e

echo "[entrypoint] cwd=$(pwd) python=$(python --version 2>&1)"

# Allow the platform (Railway, fly.io, etc.) to inject the port.
PORT="${PORT:-8000}"

echo "[entrypoint] Running alembic upgrade head..."
alembic upgrade head

echo "[entrypoint] Starting uvicorn on 0.0.0.0:${PORT}..."
exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT}" --no-server-header "$@"
