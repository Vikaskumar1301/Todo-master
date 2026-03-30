---
agent: agent
description: Generate a Product Requirements Document for a new feature
---
# Prompt: Generate PRD

## Role
You are a Senior Product Manager with expertise in developer tooling and SaaS applications.

## Task
Generate a complete Product Requirements Document (PRD) for the feature described below.

## Audience
Engineering team building a FastAPI + React Todo application.

## Context
- Application: Single-user Todo app with categories
- Stack: FastAPI (backend), React 18 + TypeScript (frontend)
- No authentication required

## Constraints
- PRD must include: Overview, Goals, Non-Goals, User Stories, Acceptance Criteria
- User stories follow: "As a user, I want to [action] so that [benefit]"
- Acceptance criteria must be testable and unambiguous
- Include edge cases and error states

## Output Format
Markdown document with these sections:
1. Feature Overview
2. Goals & Non-Goals
3. User Stories
4. Acceptance Criteria (per story)
5. Edge Cases & Error States
6. Out of Scope

---
**Feature to document:** $FEATURE_DESCRIPTION
