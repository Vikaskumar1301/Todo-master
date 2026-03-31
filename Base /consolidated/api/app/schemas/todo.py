"""Pydantic v2 schemas for the Todo resource."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TodoBase(BaseModel):
    """Shared fields for Todo create and update schemas."""

    title: str = Field(..., min_length=1, max_length=255, description="Todo title")
    description: str | None = Field(None, max_length=1000, description="Optional detail")
    category_id: int | None = Field(None, description="Optional category assignment")


class TodoCreate(TodoBase):
    """Schema for creating a new Todo."""
    pass


class TodoUpdate(BaseModel):
    """Schema for partially updating an existing Todo.

    All fields are optional — only provided fields will be updated.
    """

    title: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = Field(None, max_length=1000)
    is_completed: bool | None = None
    category_id: int | None = None


class TodoResponse(TodoBase):
    """Schema for Todo API responses."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    is_completed: bool
    created_at: datetime
    updated_at: datetime
