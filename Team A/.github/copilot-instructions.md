# GitHub Copilot — Workspace-Wide Custom Instructions
# Applies to ALL files in this monorepo.

## Project Overview
Full-stack Todo application. Monorepo with /api (FastAPI) and /web (React).
Single-user, no authentication. Enterprise-grade code quality standards.

## Universal Rules (Backend + Frontend)
- All code must include type hints / TypeScript types. No `any` in TS, no untyped Python.
- Every function/method needs a docstring (Python) or JSDoc comment (TypeScript).
- Never hardcode secrets, passwords, or connection strings. Use environment variables.
- All async operations must use proper async/await. No mixing of sync/async.
- Meaningful names: variables, functions, files. No abbreviations like `tmp`, `x`, `d`.
- Error handling is mandatory: every I/O operation, every API call, every DB query.
- Log errors with context. Never use bare `except:` or catch-all `catch(e) {}`.

## Backend (Python/FastAPI) — Architecture Rules
Strict 3-layer architecture. Violations will cause PR rejection.

LAYER RULES (non-negotiable):
  Routes (app/routes/)      → HTTP only. No DB, no business logic.
  Services (app/services/)  → Business logic only. No SQLAlchemy. No HTTP beyond HTTPException.
  Repositories (app/repositories/) → SQLAlchemy only. No business logic. No HTTP.

- Use SQLAlchemy 2.x async patterns: AsyncSession, async_sessionmaker, create_async_engine.
- All repository and service methods must be `async def`.
- Dependency injection via FastAPI `Depends()` — always inject, never instantiate directly.
- Pydantic v2 schemas for all request/response DTOs.
- HTTP status codes must be semantically correct (201 for create, 204 for delete, 404 for missing).
- Use Python logging module, not print(). Log at appropriate levels (INFO, WARNING, ERROR).

## Frontend (React/TypeScript) — Architecture Rules
  Pages (src/pages/)        → Route-level components only. No inline data fetching.
  Components (src/components/) → Reusable, dumb UI components. Accept props, emit events.
  Hooks (src/hooks/)        → All React Query logic lives here, one file per domain.
  Services (src/services/)  → Axios functions only. No React, no hooks.
  Types (src/types/)        → All TypeScript interfaces. No inline type definitions in components.

- Use React Query (TanStack) for all server state. No raw useEffect for data fetching.
- All API calls go through src/services/. Never call axios directly in a component.
- Prefer functional components and hooks. No class components.
- Use const arrow functions for components: `const MyComponent: React.FC<Props> = () => {}`
