from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- Pydantic Model ---


class Student(BaseModel):
    id: int
    name: str
    grade: int
    email: str


# --- In-Memory Data Store ---

students: list[Student] = []

# --- Endpoints ---

# TODO: Implement GET / endpoint that returns a welcome message


# TODO: Implement GET /students endpoint that returns all students


# TODO: Implement GET /students/{id} endpoint that returns a student by ID


# TODO: Implement POST /students endpoint that creates a new student


# TODO: Implement PUT /students/{id} endpoint that updates a student


# TODO: Implement DELETE /students/{id} endpoint that deletes a student
