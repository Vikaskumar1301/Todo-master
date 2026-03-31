---
applyTo: "api/**"
---
# Copilot Instructions — FastAPI Backend (/api)

## Python Standards
- Python 3.11+. Use `match` statements over long if/elif chains where appropriate.
- f-strings for string formatting. No % formatting or .format().
- Type hints on ALL function signatures including return types.
- Dataclasses or Pydantic models for structured data. No plain dicts as return values.

## FastAPI Specifics
- Router files use APIRouter with a prefix and tags list.
- Response models declared on every endpoint decorator.
- Use `status` from fastapi for status codes: `status.HTTP_201_CREATED`.
- Path operations must have summary and description in the decorator.

## SQLAlchemy 2.x Async Patterns
- Use `select()`, `update()`, `delete()` from sqlalchemy — NOT legacy Query API.
- Always `await session.execute(stmt)` then `.scalars().first()` or `.scalars().all()`.
- Models inherit from a shared `Base = DeclarativeBase()`.
- Column definitions use `mapped_column()` with `Mapped[type]` annotations.

## Alembic
- Every schema change requires a migration. Never modify DB manually.
- Migration message must describe what changed: "add_priority_column_to_todos".

## Error Handling
- Raise `HTTPException` in services only. Repositories raise plain Python exceptions.
- Always include a `detail` string in HTTPException.
- Log before raising: `logger.warning("Todo %s not found", todo_id)`.
