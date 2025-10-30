# Codex Dashboard

This repository contains a full-stack prototype for the Codex Dashboard, aligning with the implementation plan in `plan.md`.

## Structure

- `backend/`: FastAPI application skeleton with SQLAlchemy models, routers, and service placeholders.
- `frontend/`: Next.js App Router project with authentication and dashboard UI scaffolding.
- `.env.example`: Environment variable template for local development.

## Getting Started

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Testing

Backend and frontend both include placeholder tests to be completed as functionality is implemented.
