# CLAUDE.md – AYDI Project Context

## What This Project Is

AYDI (AI Yacht Design Intelligence) is a domain-specific analysis platform for yacht shipyards. It analyzes existing yacht layout designs and provides structured feedback on ergonomics, spatial efficiency, emotional room impact, regulatory compliance, and production feasibility. It does NOT generate designs — it diagnoses and improves them.

The core differentiator is boat-class-specific evaluation logic: an 8m sailboat is judged by completely different criteria than a 25m motor yacht. The same passage width that's acceptable on a small sailboat may be critically narrow on a superyacht.

## Development Commands

```bash
# Start everything
docker compose up -d

# Backend only (local dev)
cd backend
pip install -r requirements.txt
PYTHONPATH=. uvicorn app.main:app --reload

# Run tests
cd backend
PYTHONPATH=. pytest tests/ -v

# Frontend only
cd frontend
npm install
npm run dev
```

## Conventions

- All API routes prefixed with `/api/v1/`
- Async everywhere (async SQLAlchemy sessions)
- Pydantic v2 with `model_config = ConfigDict(from_attributes=True)`
- Analysis modules are pure functions — no database access
- All coordinates in millimeters, all scores 0-100
- German for user-facing strings, English for code
- boat_class: small_sail | cruising_sail | large_motor | superyacht
