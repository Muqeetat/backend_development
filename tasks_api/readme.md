# Task Management API Documentation

## Overview

The **Task Management API** is built using FastAPI and PostgreSQL. It provides endpoints for user authentication and task management. The API supports user registration, login, task creation, updating, deletion, and categorization.

## Project Structure

```
taskapi/
│── alembic/            # Database migration folder
│── app/
│   ├── routers/
│   │   ├── auth.py     # Authentication routes
│   │   ├── tasks.py    # Task management routes
│   │   ├── users.py    # User management routes
│   ├── config.py       # Configuration settings
│   ├── database.py     # Database connection setup
│   ├── main.py         # Application entry point
│   ├── models.py       # Database models
│   ├── oauth2.py       # OAuth2 authentication utilities
│   ├── utils.py        # Helper functions
│── scripts/            # Additional scripts (if any)
│── tests/              # Test cases for the API
│── requirements.txt    # Project dependencies
```

## Installation

### Prerequisites

- Python 3.9+
- PostgreSQL
- Virtual Environment (optional but recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd taskapi
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables (example for `.env` file):
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/taskdb
   SECRET_KEY=your_secret_key
   ```
5. Apply database migrations:
   ```bash
   alembic upgrade head
   ```
6. Run the API:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

### Authentication (auth.py)

#### Login User

- **Endpoint:** `POST /login`
- **Request Body:**
  ```json
  {
    "username": "testuser",
    "password": "securepassword"
  }
  ```
- **Response:**
  ```json
  {
    "access_token": "jwt_token",
    "token_type": "bearer"
  }
  ```
#### User (user.py)
 
### 1️⃣ Create a User

- **Endpoint:** `POST /users/`

 **Request Body:**
- **Content-Type:** `application/json`
- **Body Parameters:**
  ```json
  {
    "name": "testuser",
    "password": "securepassword"
  }
  ```

**Response:  (Success - `201 Created`)**
```json
{
  "id": 1,
  "name": "testuser",
  "create_date": "2025-02-12T14:00:00"
}
```
### Get User by ID

- **Endpoint:** `GET /users/{id}`
- **Description:** Retrieves user details by user ID.
- **Status Code:** `200 OK`

 **Request Body:**
```bash
curl -X GET "http://127.0.0.1:8000/users/1"
```

**Response: (Success - `200 OK`)**
```json
{
  "id": 1,
  "name": "testuser",
  "create_date": "2025-02-12T14:00:00"
}
```
### Task Management (task.py)

#### Get All Tasks

- **Endpoint:** `GET /tasks`
- **Headers:** `Authorization: Bearer <token>`
- **Query Parameters:**
  - `limit`: Optional, default `10`, maximum `100`
  - `skip`: Optional, default `0`, minimum `0`
  - `search`: Optional, search keyword for task title
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Complete API Documentation",
      "description": "Write documentation for Task API",
      "category": "Development",
      "status": "pending",
      "due_date": "2025-02-12T12:00:00",
      "create_date": "2025-02-12T12:00:00",
      "owner_id": 1,
      "owner": "UserName"
    }
  ]
  ```

#### Get Task by ID

- **Endpoint:** `GET /tasks/{id}`
- **Headers:** `Authorization: Bearer <token>`
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Complete API Documentation",
    "description": "Write documentation for Task API",
    "category": "Development",
    "status": "pending",
    "due_date": "2025-02-12T12:00:00",
    "create_date": "2025-02-12T12:00:00",
    "owner_id": 1,
    "owner": {
		"id": 1,
		"name": "username"
	}
  }
  ```

#### Get Tasks by Category

- **Endpoint:** `GET /tasks/category/{category}`
- **Headers:** `Authorization: Bearer <token>`
- **Query Parameters:**
  - `limit`: Optional, default `10`, maximum `100`
  - `skip`: Optional, default `0`, minimum `0`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Complete API Documentation",
      "description": "Write documentation for Task API",
      "category": "Development",
      "status": "pending",
      "due_date": "2025-02-12T12:00:00",
      "create_date": "2025-02-12T12:00:00",
      "owner_id": 1,
      "owner": {
		"id": 1,
		"name": "username"
	}
    }
  ]
  ```

#### Get Tasks by Username

- **Endpoint:** `GET /tasks/user/{username}`
- **Headers:** `Authorization: Bearer <token>`
- **Query Parameters:**
  - `limit`: Optional, default `10`, maximum `100`
  - `skip`: Optional, default `0`, minimum `0`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Complete API Documentation",
      "description": "Write documentation for Task API",
      "category": "Development",
      "status": "pending",
      "due_date": "2025-02-12T12:00:00",
      "create_date": "2025-02-12T12:00:00",
      "owner_id": 1,
      "owner": {
		"id": 1,
		"name": "username"
	}
    }
  ]
  ```

#### Create a Task

- **Endpoint:** `POST /tasks`
- **Headers:** `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "title": "Complete API Documentation",
    "description": "Write documentation for Task API",
    "category": "Development",
    "status": "in-progress",
    "due_date": "2025-02-12T12:00:00"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Complete API Documentation",
    "description": "Write documentation for Task API",
    "category": "Development",
    "status": "in-progress",
    "due_date": "2025-02-12T12:00:00",
    "create_date": "2025-02-12T12:00:00",
    "owner_id": 1,
    "owner": {
		"id": 1,
		"name": "username"
	}
  }
  ```

#### Update a Task

- **Endpoint:** `PUT /tasks/{id}`
- **Headers:** `Authorization: Bearer <token>`
- **Request Body:**
  ```json
  {
    "title": "Update API Documentation",
    "status": "done"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "title": "Update API Documentation",
    "description": "Write documentation for Task API",
    "category": "Development",
    "status": "completed",
    "due_date": "2025-02-12T12:00:00",
    "create_date": "2025-02-12T12:00:00",
    "owner_id": 1,
    "owner": {
		"id": 1,
		"name": "username"
	}
  }
  ```

#### Delete a Task

- **Endpoint:** `DELETE /tasks/{id}`
- **Headers:** `Authorization: Bearer <token>`
- **Response:**
  ```json
  {
    "message": "Task deleted successfully"
  }
  ```

## Running Tests

To run tests:

```bash
pytest -v -s
```

### Use following link to use the API

```json
http://127.0.0.1:8000/docs 
```