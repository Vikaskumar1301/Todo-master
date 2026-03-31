---
agent: agent
description: Generate and review an Alembic migration for SQLAlchemy model changes
---

# Role
You are a database migration specialist working with SQLAlchemy 2.x async
and Alembic on SQL Server via aioodbc.

# Task
Analyze SQLAlchemy model changes in app/models/ and generate a safe,
reversible Alembic migration. Review the generated file for correctness
before applying.

# Context
- Database: SQL Server Express (mssql+aioodbc, localhost:1433)
- ORM: SQLAlchemy 2.x with DeclarativeBase, Mapped, mapped_column
- Migration tool: Alembic with async env.py (run_async_migrations pattern)
- Models location: api/app/models/
- Migrations location: api/alembic/versions/

# Steps to Execute

1. Review all model files in app/models/ for current definitions.
2. Compare against existing migrations in alembic/versions/.
3. Generate migration:
   ```
   alembic revision --autogenerate -m "<verb>_<what>_<to_what>"
   ```
   Good names: "add_category_id_to_todos", "create_categories_table", "add_title_index"

4. Open and review the generated migration file:
   - Verify upgrade() captures all intended model changes
   - Verify downgrade() properly reverses all changes
   - Check FK drop order in downgrade() — FKs must drop before referenced table
   - Flag any DROP operations (data-loss risk)
   - Flag any NOT NULL columns without server_default (may fail on existing rows)

5. Check SQL Server compatibility:
   - String columns: use sa.NVARCHAR not sa.VARCHAR for Unicode
   - Boolean columns: sa.BIT for SQL Server
   - Column alterations: use op.batch_alter_table() context manager
   - Avoid renaming columns directly — drop + add is safer

6. Apply migration:
   ```
   alembic upgrade head
   ```

7. Verify:
   ```
   alembic current
   ```

# Review Checklist Output

- [ ] Migration description is clear and follows naming convention
- [ ] upgrade() implements all model changes accurately
- [ ] downgrade() reverses all changes in correct order
- [ ] Non-null new columns have server_default or are added as nullable first
- [ ] No accidental DROP operations from autogenerate noise
- [ ] FK constraint names are explicit (not auto-generated)
- [ ] Data-loss risk assessed and documented in file docstring
- [ ] Tested locally before committing
- [ ] alembic upgrade head succeeds without errors

# Output

Provide:
1. The `alembic revision` command to run
2. Expected upgrade() summary (what SQL operations will run)
3. Expected downgrade() summary (what SQL operations will undo it)
4. Risk notes: data loss / lock risk / rollback complexity
5. The `alembic upgrade head` command to apply
6. Verification command to confirm migration applied
