"""Pydantic v2 schemas for the Category resource."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CategoryBase(BaseModel):
    """Shared fields for Category create and update schemas."""

    name: str = Field(..., min_length=1, max_length=100, description="Category name (unique)")
    description: str | None = Field(None, max_length=500, description="Optional description")


class CategoryCreate(CategoryBase):
    """Schema for creating a new Category."""
    pass


class CategoryUpdate(BaseModel):
    """Schema for partially updating an existing Category."""

    name: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = Field(None, max_length=500)


class CategoryResponse(CategoryBase):
    """Schema for Category API responses."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
