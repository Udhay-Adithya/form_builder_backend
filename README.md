# Formflow Backend API

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A robust and scalable backend API for creating, managing, and collecting responses for dynamic forms. Built with modern Python technologies.

## ✨ Features

*   **User Management:** Secure user registration and JWT-based authentication.
*   **Dynamic Forms:** Define complex form structures with various field types (text, email, multiple choice, etc.) via JSON.
*   **Form CRUD:** Full Create, Read, Update, and Delete operations for forms, restricted to owners.
*   **Response Handling:** Submit responses to forms and retrieve collected responses (owner-only access).
*   **Asynchronous:** Built with `asyncio`, `FastAPI`, and `SQLAlchemy`'s async support for high performance.
*   **Data Validation:** Leverages Pydantic for robust request and response data validation.
*   **Database Migrations:** Uses Alembic for managing database schema changes.
*   **Dependency Injection:** Makes use of FastAPI's dependency injection system for cleaner code and easier testing.

## 🛠️ Tech Stack

*   **Backend Framework:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Database ORM:** [SQLAlchemy](https://www.sqlalchemy.org/) (with async support)
*   **Database:** [PostgreSQL](https://www.postgresql.org/) (using `asyncpg` driver)
*   **Data Validation:** [Pydantic](https://pydantic-docs.helpmanual.io/)
*   **Migrations:** [Alembic](https://alembic.sqlalchemy.org/)
*   **Authentication:** JWT with [python-jose](https://github.com/mpdavis/python-jose) and [passlib](https://passlib.readthedocs.io/)
*   **ASGI Server:** [Uvicorn](https://www.uvicorn.org/)

## 📂 Project Structure

```
form_builder_backend/
├── alembic/                   # Alembic migration scripts
│   ├── versions/
│   └── env.py
├── app/                       # Main application source code
│   ├── api/                   # API endpoints (routers)
│   │   └── v1/
│   │       ├── endpoints/     # Specific endpoint logic
│   │       └── api.py         # API router aggregation
│   ├── core/                  # Core components (config, security)
│   ├── crud/                  # Database interaction logic (CRUD operations)
│   ├── db/                    # Database setup (session, base model)
│   ├── models/                # SQLAlchemy ORM models
│   ├── schemas/               # Pydantic schemas (data validation)
│   ├── dependencies.py        # FastAPI dependencies
│   └── main.py                # FastAPI application entry point
├── .env                       # Environment variables (create this file)
├── .gitignore                 # Git ignore rules
├── alembic.ini                # Alembic configuration
├── requirements.txt           # Project dependencies
└── README.md                  # This file
```

## 🚀 Getting Started

### Prerequisites

*   Python 3.10 or higher
*   PostgreSQL Server (running locally or accessible)
*   Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Udhay-Adithya/formflow_backend
    cd form_builder_backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On macOS/Linux
    source venv/bin/activate
    # On Windows
    # venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the project root directory. Copy the contents from `.env.example` (if provided) or add the following variables, adjusting values as needed:

    ```dotenv
    # .env
    PROJECT_NAME="Formflow"

    # PostgreSQL Database URL
    # Format: postgresql+asyncpg://<user>:<password>@<host>:<port>/<database_name>
    DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/formflow_db

    # JWT Settings
    SECRET_KEY=your_super_secret_key_change_this # Generate a strong secret key (e.g., using openssl rand -hex 32)
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=60
    ```
    *   Ensure the specified PostgreSQL database exists or create it.

5.  **Run Database Migrations:**
    Apply the latest database schema changes using Alembic:
    ```bash
    alembic upgrade head
    ```

### Running the Application

Start the development server using Uvicorn:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

*   `--reload`: Enables auto-reloading on code changes (for development).
*   `--host 0.0.0.0`: Makes the server accessible on your local network.
*   `--port 8000`: Specifies the port to run on.

The API will be available at `http://localhost:8000`.

## 📚 API Documentation

Once the server is running, interactive API documentation is available at:

*   **Swagger UI:** `http://localhost:8000/docs`
*   **ReDoc:** `http://localhost:8000/redoc`

These interfaces allow you to explore and interact with all available API endpoints.

### Main API Endpoint Groups

*   `/api/v1/auth`: User registration and token generation (login).
*   `/api/v1/users`: User-related operations (e.g., getting the current user).
*   `/api/v1/forms`: CRUD operations for forms.
*   `/api/v1/forms/{form_id}/responses`: Submitting and retrieving responses for a specific form.

## 🧪 Running Tests (TODO)

*(Instructions for running tests will be added here once test suites are implemented.)*

## 🤝 Contributing

Contributions are welcome! Please follow standard fork-and-pull-request workflow. Ensure your code adheres to the project's style and includes tests for new features or bug fixes.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. *(Create a LICENSE file, e.g., containing the MIT License text)*