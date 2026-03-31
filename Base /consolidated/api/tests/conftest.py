"""Shared pytest fixtures for the test suite."""

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app


@pytest.fixture
def anyio_backend() -> str:
    """Use asyncio backend for pytest-asyncio."""
    return "asyncio"


@pytest.fixture
async def async_client() -> AsyncClient:
    """AsyncClient wired to the FastAPI app via ASGI transport.

    Use for route-level integration tests.
    """
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as client:
        yield client


@pytest.fixture
def sample_todo_create() -> dict:
    """Sample valid TodoCreate payload."""
    return {"title": "Buy groceries", "description": "Milk, eggs, bread"}


@pytest.fixture
def sample_category_create() -> dict:
    """Sample valid CategoryCreate payload."""
    return {"name": "Shopping", "description": "Errands and shopping tasks"}
