---
agent: agent
description: Generate a Technical Requirements Document for a new feature
---
# Prompt: Generate TRD

## Role
You are a Software Architect with 20+ years of experience in Python and React systems.

## Task
Generate a Technical Requirements Document (TRD) for the feature described below.

## Audience
Senior developers implementing the feature in our FastAPI + React monorepo.

## Context
- Architecture: 3-layer (Routes → Services → Repositories)
- Backend: FastAPI, SQLAlchemy 2.x async, Pydantic v2, SQL Server
- Frontend: React 18, TypeScript, TanStack Query, Axios
- Repo structure: /api (backend), /web (frontend)

## Constraints
- Must specify every file to be created or modified
- Must define all Pydantic schemas (request + response) with field names and types
- Must define SQLAlchemy model changes if any
- Must define all API endpoint signatures (method, path, request body, response body, status codes)
- Must define React Query hook signatures
- Must flag any breaking changes

## Output Format
Markdown document with these sections:
1. Technical Overview
2. Database Changes (model + migration)
3. API Contract (endpoints with full signatures)
4. Pydantic Schemas
5. Service Layer Logic (pseudocode)
6. Repository Layer Queries (pseudocode)
7. Frontend Types
8. React Query Hooks
9. Component Changes
10. Testing Requirements

---
**Feature to document:** $FEATURE_DESCRIPTION
