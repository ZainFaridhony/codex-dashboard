# Full-Stack Web Application Plan

## Checklist
- Parse functional requirements for authentication, dashboard interactions, and integrations.
- Map component interactions across frontend, backend, database, and Brevo.
- Specify REST endpoints, payloads, errors, and supporting schema design.
- Detail authentication flows (local, OAuth, password reset) alongside security controls.
- Outline testing matrix and implementation sequencing through deployment preparation.

## 1. High-Level Architecture Diagram Description
- **Frontend (Next.js + UI Library)**: Presents registration/login forms, handles Google OAuth initiation, renders dashboard SPA, manages in-memory access tokens and relies on HttpOnly cookies for refresh tokens, and polls backend for email verification status.
- **Backend API (FastAPI)**: Exposes authentication, OAuth, password reset, and dashboard endpoints; orchestrates JWT issuance/refresh, interacts with PostgreSQL via SQLAlchemy, triggers Brevo emails, aggregates dashboard data, and enforces RBAC middleware.
- **Database (PostgreSQL)**: Persists users, OAuth links, hashed passwords, refresh and reset tokens, dashboard widgets, user preferences, and audit logs with strict constraints.
- **Email Service (Brevo via API)**: Receives password reset (and optional verification) requests from backend through Brevo SDK/HTTP; delivers templated emails containing secure reset links.
- **Interactions**: Frontend calls FastAPI for auth and dashboard data; FastAPI validates/executes business logic, persists/retrieves from PostgreSQL, and invokes Brevo when password reset events occur; Google OAuth redirect/callback sequence completes via backend before issuing tokens to frontend.

Validation: All mandated components and their interactions are covered without omissions.

## 2. Detailed Technical Specifications

### API Endpoints
- `POST /api/auth/register`  
  Request `{ email:str (required), password:str (≥12 chars), first_name:str, last_name:str }`  
  Response `201` `{ user_id:uuid, email, profile_completed:bool }`, optional `Set-Cookie` refresh token  
  Errors: `400` validation failure, `409` duplicate email, `422` password policy violation  
  Sample request `{"email":"user@demo.io","password":"S3curePass!234","first_name":"Ayo","last_name":"Lee"}`

- `POST /api/auth/login`  
  Request `{ email:str, password:str }`  
  Response `200` `{ access_token:str (JWT), expires_in:int, refresh_token?:str }`  
  Errors: `401` invalid credentials, `423` account locked, `429` rate limited

- `POST /api/auth/logout`  
  Clears HttpOnly refresh cookie, revokes associated server token entry  
  Response `204` empty  
  Errors: `401` unauthenticated

- `POST /api/auth/token/refresh`  
  Request via `Cookie: refresh_token=<uuid>` or body `{ refresh_token:str }`  
  Response `200` `{ access_token:str, expires_in:int }`  
  Errors: `401` invalid/expired token, `409` rotation failure

- `GET /api/auth/me`  
  Authenticated via Bearer token  
  Response `200` `{ user_id, email, first_name, last_name, roles:[str], last_login:datetime }`  
  Errors: `401` unauthenticated, `403` forbidden

- `GET /api/auth/google/authorize`  
  Query `redirect_uri`  
  Response `302` redirect to Google OAuth URL  
  Errors: `400` invalid redirect URI/state generation failure

- `GET /api/auth/google/callback`  
  Query `code`, `state`  
  Response `302` redirect to frontend success route after token issuance  
  Errors: `400` invalid state, `401` exchange failure

- `POST /api/auth/password/forgot`  
  Request `{ email:str }`  
  Response `202` accepted (blind for enumeration protection)  
  Errors: `429` throttled

- `POST /api/auth/password/reset`  
  Request `{ token:str (uuid), password:str }`  
  Response `200` `{ message:"Password updated" }`  
  Errors: `400` invalid token, `410` expired token, `422` password policy violation

- `GET /api/dashboard/overview`  
  Query `date_range`, optional filters  
  Response `200` `{ user:{first_name,last_login}, stats:{logins_30d:int,tasks_completed:int}, widgets:[{id,type,data}] }`  
  Errors: `401` unauthenticated, `403` forbidden

- `PATCH /api/dashboard/widgets/:id`  
  Request `{ config:JSON, position:int, version:int }`  
  Response `200` updated widget payload  
  Errors: `404` not found, `409` version conflict

- Error payload format for all endpoints: `{ "error": { "code": "string_identifier", "message": "Human readable", "details": {...} } }`

### Database Schema
- `users`: `id UUID PK`, `email CITEXT UNIQUE`, `password_hash TEXT nullable (OAuth-only)`, `first_name TEXT`, `last_name TEXT`, `is_active BOOLEAN DEFAULT true`, `is_email_verified BOOLEAN DEFAULT false`, `created_at TIMESTAMPTZ DEFAULT now`, `updated_at TIMESTAMPTZ`
- `oauth_accounts`: `id UUID PK`, `user_id UUID FK users(id) ON DELETE CASCADE`, `provider TEXT`, `provider_account_id TEXT`, `access_token TEXT`, `refresh_token TEXT`, `expires_at TIMESTAMPTZ`, `UNIQUE(provider, provider_account_id)`
- `refresh_tokens`: `id UUID PK`, `user_id UUID FK users(id)`, `token_hash TEXT UNIQUE`, `created_at TIMESTAMPTZ`, `expires_at TIMESTAMPTZ`, `revoked BOOLEAN DEFAULT false`
- `password_reset_tokens`: `id UUID PK`, `user_id UUID FK users(id)`, `token_hash TEXT UNIQUE`, `requested_at TIMESTAMPTZ`, `expires_at TIMESTAMPTZ`, `used_at TIMESTAMPTZ`
- `user_profiles`: `user_id UUID PK FK users(id)`, `avatar_url TEXT`, `time_zone TEXT`, `preferences JSONB`
- `dashboard_widgets`: `id UUID PK`, `user_id UUID FK users(id)`, `type TEXT`, `config JSONB`, `position INT`, `updated_at TIMESTAMPTZ`
- `audit_logs`: `id UUID PK`, `user_id UUID FK users(id)`, `action TEXT`, `ip INET`, `metadata JSONB`, `created_at TIMESTAMPTZ`

### Backend File Structure
```text
backend/
  app/
    main.py
    config.py
    dependencies.py
    db/
      session.py
      models/
        __init__.py
        user.py
        oauth.py
        tokens.py
        dashboard.py
    schemas/
      auth.py
      user.py
      dashboard.py
    routers/
      auth.py
      google_oauth.py
      password_reset.py
      dashboard.py
    services/
      auth.py
      oauth.py
      email.py
      dashboard.py
      security.py
    utils/
      tokens.py
      rate_limiter.py
    tests/
      conftest.py
      test_auth.py
      test_dashboard.py
      integration/
```

### Frontend File Structure
```text
frontend/
  app/
    layout.tsx
    page.tsx
    dashboard/
      page.tsx
      components/
        DashboardShell.tsx
        WidgetCard.tsx
    auth/
      login/page.tsx
      register/page.tsx
      forgot-password/page.tsx
      reset-password/[token]/page.tsx
    api/
      auth.ts
      dashboard.ts
  lib/
    auth.ts
    httpClient.ts
    validators.ts
  components/
    forms/
    layout/
  styles/
    globals.css
    theme.ts
  hooks/
    useAuth.ts
    useDashboard.ts
  tests/
    auth.test.tsx
    dashboard.test.tsx
```

### Critical Dependencies
- **Backend**: `fastapi`, `uvicorn`, `sqlalchemy>=2.0`, `asyncpg`, `alembic`, `pydantic`, `passlib[bcrypt]`, `argon2-cffi` (optional), `python-jose`, `Authlib`, `httpx`, `redis`, `python-brevo` (or `sib-api-v3-sdk`), `sentry-sdk`, `pytest`, `pytest-asyncio`, `pytest-cov`, `faker`
- **Frontend**: `next@14`, `react@18`, `typescript`, `@shadcn/ui` (or `@chakra-ui/react`), `react-hook-form`, `zod`, `axios` or `ky`, `swr` or `@tanstack/react-query`, `jest`, `@testing-library/react`, `msw`, `eslint`, `prettier`

Validation: Section enumerates endpoints, schema, file structures, and dependencies as required; no noticeable gaps.

## 3. Authentication Flow Explanation
- **Local registration/login**: Frontend validates input with zod, calls `POST /api/auth/register`; backend hashes password (bcrypt/argon2), stores user, optionally sets refresh token cookie, issues short-lived access token. Login path verifies hash via `POST /api/auth/login`, checks `is_active`, logs event, returns tokens; frontend stores access token in memory/context and relies on HttpOnly refresh cookie for rotation via `/api/auth/token/refresh`.
- **Google OAuth sign-in**: Frontend hits `/api/auth/google/authorize` to retrieve Google consent redirect; user authenticates with Google which returns to `/api/auth/google/callback`; backend exchanges code using Authlib, upserts user, links `oauth_accounts`, issues tokens, sets refresh cookie, and redirects to frontend which finalizes session by calling `/api/auth/me`.
- **Forgot-password (Brevo)**: Frontend posts email to `/api/auth/password/forgot`; backend generates random token (stored hashed with expiry), triggers Brevo transactional template containing `https://frontend/reset-password/{token}`; user follows link, submits new password to `/api/auth/password/reset`, backend validates token (unused, unexpired), hashes new password, revokes old refresh tokens, marks token used, responds success; frontend navigates back to login.

Validation: All requested authentication paths are described sequentially end-to-end.

## 4. Security Measures and Testing Strategy
- **Security Controls**: Password hashing via Argon2id or bcrypt with per-user salt; JWT access tokens signed with RS256 private key (stored securely) with 15-minute expiry; refresh token rotation stored hashed in DB; enforce HTTPS with Secure+HttpOnly+SameSite=strict cookies; CSRF protection using double-submit tokens for state-changing requests; request throttling for login/forgot-password through Redis-backed rate limiter; input validation using Pydantic/zod; SQL injection prevention via SQLAlchemy parameter binding; audit logging of auth events; strict CORS allowlist; Google OAuth state nonce stored server-side; password reset links single-use with IP/device logging; environment secrets managed via rotated `.env` managed store.
- **Testing Strategy**: Pytest unit tests for services (hashing, token lifecycle, email adapter), API tests via `httpx.AsyncClient` for happy/bad paths, integration tests with transactional Postgres, contract tests verifying response schemas, security regression tests (expired tokens, replay, CSRF), performance checks using `locust`, frontend Jest/RTL tests for forms and hooks, MSW-powered integration tests, CI enforcing coverage thresholds (backend ≥90%, frontend ≥85%) with `pytest-cov` and `jest --coverage`.

Validation: Security and testing coverage align with requirements; no key measure appears missing.

## 5. Step-by-Step Implementation Plan
1. **Environment Setup** – Configure Python 3.13 venv, Node 20 workspace, Dockerized Postgres, and `.env.example` files. *Deliverable*: Working dev environment with documented environment variables.
2. **Backend Scaffolding** – Initialize FastAPI project structure, config management, DB session, Alembic migrations. *Deliverable*: Running FastAPI app with health endpoint and migration tooling.
3. **Database Modeling** – Define SQLAlchemy models and initial migrations for auth, profiles, dashboard entities. *Deliverable*: Migration applied to dev DB.
4. **Auth Core (Local)** – Implement registration/login/logout, password hashing, JWT/refresh services, `/me`. *Deliverable*: Passing backend tests for local auth flows.
5. **Google OAuth Integration** – Configure Authlib, manage state, process callback, link/create users. *Deliverable*: Google OAuth login verified locally.
6. **Brevo Password Reset** – Build email service wrapper and forgot/reset endpoints with templates. *Deliverable*: End-to-end password reset flow tested via Brevo sandbox.
7. **Dashboard API** – Implement overview and widget endpoints with RBAC checks and aggregation. *Deliverable*: Dashboard responses returning fixture data with tests.
8. **Frontend Scaffolding** – Create Next.js app, configure UI library, routing, layout, HTTP client. *Deliverable*: Static pages rendering in development.
9. **Frontend Auth UI** – Build register/login/forgot/reset pages, token handling hooks, OAuth redirect handling. *Deliverable*: Auth screens integrated with backend.
10. **Dashboard UI** – Implement dashboard shell, widget components, and data fetching hooks. *Deliverable*: Functional dashboard with dynamic data.
11. **Hardening & QA** – Add rate limiting, audit logging, error handling, finalize security tests, run end-to-end smoke tests (Playwright). *Deliverable*: Green test suite with coverage reports.
12. **Deployment Preparation** – Create Dockerfiles, docker-compose, CI workflows, and deployment runbook. *Deliverable*: Automated pipeline configs and deployment guide.

Validation: Implementation roadmap flows logically from setup through deployment with clear objectives and deliverables.

## Next Steps
1. Stand up the development environment outlined in Step 1.  
2. Acquire Google OAuth and Brevo API credentials to unblock integrations.
