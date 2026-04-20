# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using Python's FastAPI framework. You will create a simple API that handles CRUD operations for a resource, apply request validation, and return structured JSON responses.

## 📝 Tasks

### 🛠️	Set Up a FastAPI Project

#### Description
Install FastAPI and Uvicorn, then create a basic FastAPI application that runs a development server and returns a welcome message at the root endpoint.

#### Requirements
Completed program should:

- Install `fastapi` and `uvicorn` using pip
- Create a `main.py` file with a FastAPI app instance
- Define a `GET /` endpoint that returns `{"message": "Welcome to the Student API"}`
- Run successfully with `uvicorn main:app --reload`

### 🛠️	Build CRUD Endpoints for a Student Resource

#### Description
Create a set of API endpoints that allow users to create, read, update, and delete student records. Each student should have an `id`, `name`, `grade`, and `email` field. Use Pydantic models for request validation.

#### Requirements
Completed program should:

- Define a `Student` Pydantic model with fields: `id` (int), `name` (str), `grade` (int), `email` (str)
- Implement `GET /students` to list all students
- Implement `GET /students/{id}` to retrieve a single student by ID
- Implement `POST /students` to create a new student with validation
- Implement `PUT /students/{id}` to update an existing student
- Implement `DELETE /students/{id}` to remove a student
- Return appropriate HTTP status codes (200, 201, 404) for each operation
