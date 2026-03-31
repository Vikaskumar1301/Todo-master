---
applyTo: "web/**"
---
# Copilot Instructions — React Frontend (/web)

## TypeScript Standards
- Strict mode enabled. No `any`, no `@ts-ignore` without a comment explaining why.
- All props must have explicit interfaces defined in src/types/.
- Use `type` for unions/primitives, `interface` for object shapes.

## React Standards
- Functional components only. Arrow function syntax.
- Custom hooks prefix: `use` (e.g., `useTodos`, `useCategories`).
- Do not derive state that can be computed from existing state.
- Keys in lists must be stable IDs, never array indices.

## React Query Patterns
- One query file per domain: src/hooks/useTodos.ts, src/hooks/useCategories.ts.
- Query keys must be arrays and descriptive: `['todos', todoId]`.
- Always handle `isLoading`, `isError`, and `data` states in components.
- Mutations must call `queryClient.invalidateQueries()` on success.

## Axios / API Layer
- Base URL from environment variable: `import.meta.env.VITE_API_URL`.
- Centralized Axios instance in src/services/api.ts.
- All service functions are async and return typed responses.
- Handle errors in service layer, re-throw with meaningful messages.

## Styling
- Use plain CSS modules or Tailwind (if configured). No inline styles except dynamic values.
