/**
 * TypeScript interfaces for the Todo domain.
 * All API request/response shapes are defined here.
 */

export interface Todo {
  id: number;
  title: string;
  description: string | null;
  isCompleted: boolean;
  categoryId: number | null;
  createdAt: string;
  updatedAt: string;
}

export interface TodoCreate {
  title: string;
  description?: string;
  categoryId?: number;
}

export interface TodoUpdate {
  title?: string;
  description?: string | null;
  isCompleted?: boolean;
  categoryId?: number | null;
}
