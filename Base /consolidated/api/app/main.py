"""FastAPI application factory — CORS, router registration, startup events."""

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.todo_router import router as todo_router
from app.routes.category_router import router as category_router

logger = logging.getLogger(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance.

    Returns:
        Configured FastAPI application with CORS, routes, and middleware.
    """
    app = FastAPI(
        title="Todo AI API",
        version="1.0.0",
        description="Enterprise-grade Todo application API with category support.",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS — allow Vite dev server
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(todo_router)
    app.include_router(category_router)

    @app.get("/health", tags=["health"])
    async def health_check() -> dict[str, str]:
        """Health check endpoint."""
        return {"status": "ok"}

    @app.on_event("startup")
    async def on_startup() -> None:
        logger.info("Todo AI API started successfully.")

    return app


app = create_app()
