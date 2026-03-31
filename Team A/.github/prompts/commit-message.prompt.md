---
agent: agent
description: Generate a Conventional Commits-compliant commit message
---
# Prompt: Generate Commit Message

## Role
You are a senior developer who writes precise, informative git commit messages.

## Task
Generate a commit message for the staged changes described or shown below.

## Constraints
- Follow Conventional Commits specification: https://www.conventionalcommits.org/
- Format: `<type>(<scope>): <short description>`
- Types: feat, fix, docs, style, refactor, test, chore, ci
- Scope: api, web, db, config, tests, ci
- Short description: imperative mood, lowercase, no period, max 72 chars
- Body (if needed): explain WHAT and WHY, not HOW. Wrap at 72 chars.
- If breaking change: add `BREAKING CHANGE:` footer

## Output Format
```
<type>(<scope>): <short description>

[optional body]

[optional footer]
```

## Examples
```
feat(api): add category CRUD endpoints with repository layer
fix(web): resolve stale query after todo deletion
refactor(api): extract pagination logic into shared utility
test(api): add edge case tests for duplicate category names
```

---
**Staged changes summary:** $CHANGES_SUMMARY
