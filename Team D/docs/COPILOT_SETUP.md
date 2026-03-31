# Copilot Customization Setup — Complete Reference

> **Last Updated:** 2026-03-31
> **Phase:** 0 — Foundation & Copilot Setup
> **Status:** All artifacts created

---

## Table of Contents

1. [Overview: The Copilot Customization Hierarchy](#overview-the-copilot-customization-hierarchy)
2. [File-by-File Breakdown](#file-by-file-breakdown)
3. [How All Files Work Together](#how-all-files-work-together)
4. [Quick Reference Table](#quick-reference-table)
5. [Usage Examples](#usage-examples)
6. [Terminology & Concepts](#terminology--concepts)

---

## Overview: The Copilot Customization Hierarchy

Think of this as a **layered system of instructions**:

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: Custom Instructions                                │
│ (.github/copilot-instructions.md)                           │
│ Always-on, workspace-wide rules                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: Language Instructions                              │
│ (.github/instructions/*.instructions.md)                    │
│ Auto-scoped by file pattern (applyTo)                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: Agents, Skills, Prompts (Manual Activation)       │
│ @api, @web, #commit-message, test-runner, etc.            │
│ You or Copilot invoke these explicitly                      │
└─────────────────────────────────────────────────────────────┘
```

### Activation Spectrum

```
Always on ◄──────────────────────────────────► Manual only

Instructions → Language Instructions → Skills → Agents → Prompt Files
(silent)       (scoped, silent)     (auto)    (invoked) (invoked)
```

---

## File-by-File Breakdown

### FILE 1: `.github/copilot-instructions.md`

**Type:** Custom Instructions (always-on)
**Scope:** Entire workspace
**Activation:** Automatic — Copilot reads this before every suggestion
**Size:** ~2 KB

#### What it is
The **workspace constitution** — a single markdown file that Copilot reads automatically on every suggestion. It defines the overall architecture and general rules that apply to all code.

#### How it works
- Copilot loads this file in the background **before generating ANY code**
- No manual invocation needed — it's **always active**
- Applies to **every file** in your repo
- Silently guides all Copilot suggestions, completions, and chat answers

#### What's inside
- Project Overview (monorepo with /api and /web)
- 3-Layer Architecture (Routes → Services → Repositories)
- Dependency Injection Flow (get_db → Repository → Service → Route)
- Backend Conventions (async, type hints, Pydantic v2, logging, status codes)
- Frontend Conventions (functional components, React Query, named exports, no `any`)
- Testing standards
- General Rules (no secrets, error handling, docstrings, Conventional Commits)

---

### FILE 2: `.github/instructions/api.instructions.md`

**Type:** Language Instructions (auto-scoped)
**Scope:** `api/**/*.py` files only
**Activation:** Automatic when editing Python files in /api

#### What it is
Python-specific coding standards that automatically activate when you edit any `.py` file under the `api/` directory.

#### What's inside
- Async Pattern: `async def` everywhere, `await` for DB operations
- Type Hints: `Optional[Model]`, `list[Model]`, `Annotated[Type, Depends()]`
- Dependency Injection: Route → Service → Repository → AsyncSession chain
- Pydantic Schemas: v2 with `ConfigDict(from_attributes=True)`, separate Create/Update/Response
- SQLAlchemy Models: `DeclarativeBase`, `Mapped[]`, `mapped_column()`
- Error Handling: Services raise `HTTPException` with detail messages
- Logging: `logging.getLogger(__name__)`, never `print()`
- Docstrings: Google style with Args, Returns, Raises
- Import Order: stdlib → third-party → local

---

### FILE 3: `.github/instructions/web.instructions.md`

**Type:** Language Instructions (auto-scoped)
**Scope:** `web/src/**/*.{ts,tsx}` files only
**Activation:** Automatic when editing TypeScript files in /web

#### What it is
TypeScript/React-specific standards that automatically activate when editing frontend files.

#### What's inside
- Component Style: Arrow functions, no class components, no `React.FC`
- Props & Types: Named interfaces in `src/types/`, no `any` type
- Data Fetching: React Query only (`useQuery`, `useMutation`), no `useState` for API data
- API Layer: Axios instance with `baseURL`, service functions return typed data
- State Management: Server state via React Query, UI state via useState
- Error & Loading States: Every data-fetching component handles `isLoading` and `isError`
- Exports: Prefer named exports, default only for page/route files
- Styling: CSS Modules or Tailwind, no inline styles

---

### FILE 4: `.github/copilot/api-agent.agent.yml`

**Type:** Custom Agent (manual invocation)
**Activation:** Manual via `@api` in Copilot Chat
**Scope:** `api/**`

#### What it is
A specialized backend expert persona. References `copilot-instructions.md` and `api.instructions.md` for consistency.

#### What's inside
- Architecture enforcement (3-layer)
- File layout (models, schemas, DB config, entry point, migrations)
- Dependency injection chain with exact wiring
- Full tech stack (Python 3.11+, FastAPI, SQLAlchemy 2.x async, SQL Server, Pydantic v2)
- Testing strategy (pytest + pytest-asyncio)
- Rules (async, type hints, logging, status codes)

---

### FILE 5: `.github/copilot/web-agent.agent.yml`

**Type:** Custom Agent (manual invocation)
**Activation:** Manual via `@web` in Copilot Chat
**Scope:** `web/**`

#### What it is
A specialized frontend expert persona. References `copilot-instructions.md` and `web.instructions.md` for consistency.

#### What's inside
- File layout (pages, components, hooks, services, types, utils)
- Data fetching pattern (Component → Hook → Service → Axios → API)
- Full tech stack (React 18, TypeScript, Vite, React Query, Axios)
- Testing strategy (Vitest + React Testing Library)
- Rules (functional components, named interfaces, no `any`, React Query for server state)

---

### FILE 6-10: `.github/prompts/*.prompt.md`

**Type:** Prompt Files (manual invocation)
**Activation:** Manual via `#<name>` in Copilot Chat

| File | Invocation | Purpose |
|------|-----------|---------|
| `commit-message.prompt.md` | `#commit-message` | Generate Conventional Commit message |
| `pr-review.prompt.md` | `#pr-review` | Pre-PR code review checklist |
| `generate-prd.prompt.md` | `#generate-prd` | Product Requirements Document |
| `generate-trd.prompt.md` | `#generate-trd` | Technical Requirements Document |
| `db-migration.prompt.md` | `#db-migration` | Alembic migration generation |

All prompts use the RTACCO pattern (Role/Task/Audience/Context/Constraints/Output).

---

### FILE 11-15: `.github/skills/*.skill.yml`

**Type:** Skills (auto-triggered or manual)

| File | Trigger | Purpose |
|------|---------|---------|
| `test-runner.skill.yml` | Tests modified or requested | Run pytest or vitest, report results |
| `api-endpoint-generation.skill.yml` | Creating routes or "generate endpoint" | Full 3-layer endpoint scaffolding |
| `database-migration.skill.yml` | Modifying models or "create migration" | Safe Alembic migration planning |
| `performance-review.skill.yml` | "Is this performant?" or pre-PR | Backend + frontend perf audit |
| `security-review.skill.yml` | "Is this secure?" or pre-PR | OWASP-aligned security audit |

---

## How All Files Work Together

### Feature Development Workflow

```
Step 1:  #generate-prd         → Define what to build (user stories, acceptance criteria)
Step 2:  #generate-trd         → Plan how to build it (files, endpoints, DI wiring)
Step 3:  @api agent            → Generate backend code (model, schema, repository)
Step 4:  api-endpoint skill    → Auto-generate route handlers with proper status codes
Step 5:  database-migration    → Auto-generate Alembic migration for schema changes
Step 6:  @web agent            → Generate frontend code (hooks, services, components)
Step 7:  test-runner skill     → Run pytest and vitest, report failures
Step 8:  #pr-review            → Pre-merge code review (triggers security + performance)
Step 9:  security-review skill → OWASP-aligned security audit
Step 10: performance-review    → Backend + frontend performance audit
Step 11: #commit-message       → Generate conventional commit message
```

### Instruction Hierarchy

```
Layer 1 (Always On):
  └─ copilot-instructions.md (workspace architecture)

Layer 2 (Auto-scoped):
  ├─ api.instructions.md (api/**/*.py)
  └─ web.instructions.md (web/src/**/*.{ts,tsx})

Layer 3 (Manual Activation):
  ├─ Agents (@api, @web)
  ├─ Prompt Files (#commit-message, #pr-review, #generate-prd, #generate-trd, #db-migration)
  └─ Skills (test-runner, api-endpoint-generation, database-migration, performance-review, security-review)
```

---

## Quick Reference Table

| # | File | Type | Activation | Purpose |
|---|------|------|-----------|---------|
| 1 | `copilot-instructions.md` | Custom Instructions | Always on | Workspace architecture rules |
| 2 | `api.instructions.md` | Language Instructions | Auto (`api/**/*.py`) | Python/FastAPI conventions |
| 3 | `web.instructions.md` | Language Instructions | Auto (`web/src/**/*.{ts,tsx}`) | React/TypeScript conventions |
| 4 | `api-agent.agent.yml` | Agent | Manual (`@api`) | Backend expert persona |
| 5 | `web-agent.agent.yml` | Agent | Manual (`@web`) | Frontend expert persona |
| 6 | `commit-message.prompt.md` | Prompt | Manual (`#commit-message`) | Conventional commit generator |
| 7 | `pr-review.prompt.md` | Prompt | Manual (`#pr-review`) | Pre-PR review checklist |
| 8 | `generate-prd.prompt.md` | Prompt | Manual (`#generate-prd`) | Product requirements doc |
| 9 | `generate-trd.prompt.md` | Prompt | Manual (`#generate-trd`) | Technical requirements doc |
| 10 | `db-migration.prompt.md` | Prompt | Manual (`#db-migration`) | Alembic migration generator |
| 11 | `test-runner.skill.yml` | Skill | Auto-triggered | Run and report test results |
| 12 | `api-endpoint-generation.skill.yml` | Skill | Auto-triggered | Generate 3-layer endpoints |
| 13 | `database-migration.skill.yml` | Skill | Auto-triggered | Plan safe schema migrations |
| 14 | `performance-review.skill.yml` | Skill | Auto-triggered | Performance audit |
| 15 | `security-review.skill.yml` | Skill | Auto-triggered | Security audit |

---

## Usage Examples

### Example 1: Building a New Feature

```
You: #generate-prd "I want to add category support so users can organize todos"
  → Copilot generates PRD with user stories, acceptance criteria, API contract

You: #generate-trd [paste PRD]
  → Copilot generates TRD with file list, DB changes, endpoint table, test plan

You: @api "Implement the Category model and repository from the TRD"
  → api-agent generates model, schemas, repository with async queries

You: @web "Create the category hooks and components from the TRD"
  → web-agent generates hooks, services, components following React Query pattern

You: "run tests"
  → test-runner skill auto-detects backend/frontend and runs appropriate suite
```

### Example 2: Pre-PR Review

```
You: #pr-review
  → Copilot reviews all changed files against architecture, security, type safety checklist
  → security-review skill checks for OWASP vulnerabilities
  → performance-review skill identifies bottlenecks

You: #commit-message
  → Copilot generates: "feat(api): add category CRUD endpoints with validation"
```

### Example 3: Database Schema Change

```
You: #db-migration "Add a priority column to the todos table"
  → Copilot reviews models, generates alembic command, reviews migration file

You: @api "Update the todo service to support filtering by priority"
  → api-agent adds filter logic following 3-layer architecture
```

---

## Terminology & Concepts

| Term | Definition |
|------|-----------|
| **Custom Instructions** | Always-on workspace rules in `copilot-instructions.md` |
| **Language Instructions** | Auto-scoped rules activated by file patterns (`applyTo`) |
| **Agent** | Specialized persona invoked via `@name` in Copilot Chat |
| **Skill** | Auto-triggered capability that runs when context matches |
| **Prompt File** | Reusable prompt template invoked via `#name` in Copilot Chat |
| **RTACCO** | Role/Task/Audience/Context/Constraints/Output — prompt structure pattern |
| **3-Layer Architecture** | Routes → Services → Repositories separation of concerns |
| **Dependency Injection** | FastAPI `Depends()` chain: get_db → Repository → Service → Route |
| **React Query** | TanStack library for server state management (caching, sync, dedup) |
| **Conventional Commits** | Commit message format: `type(scope): description` |

---

## Getting Started

1. Open the repo in VS Code with GitHub Copilot enabled.
2. `copilot-instructions.md` and language instructions activate automatically.
3. Use `@api` or `@web` agents in Copilot Chat for domain-specific help.
4. Use `#generate-prd` and `#generate-trd` to plan new features.
5. Skills auto-trigger based on context (tests, migrations, reviews).
6. Use `#pr-review` and `#commit-message` before pushing code.
