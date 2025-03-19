# Carting API

A FastAPI-based RESTful API for cart management with PostgreSQL database.

## Features

- FastAPI framework for API
- PostgreSQL database with SQLAlchemy ORM
- Connection pooling for database efficiency
- Pydantic for data validation
- Dependency injection
- Environment variable configuration
- CORS support
- Docker support for containerization
- UV package manager for dependency management
- Alembic for database migrations

## Project Structure

```
carting/
├── src/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   └── items.py
│   │   └── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db/
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── tests/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   └── models.py
├── .env
├── .gitignore
├── .python-version
├── alembic.ini
├── docker-compose.yml
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Requirements

- Python 3.11+
- PostgreSQL database
- FastAPI
- SQLAlchemy
- Uvicorn
- python-dotenv
- pydantic-settings
- psycopg2-binary
- Docker (optional)
- UV package manager

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd carting
```

2. Set up a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install dependencies using UV (recommended):

```bash
pip install uv
uv pip install -e .
```

Or using pip:

```bash
pip install -e .
```

4. Create a `.env` file with the following content:

```
DEBUG=True
HOST=0.0.0.0
PORT=8000
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/carting
# Or use individual settings
# POSTGRES_USER=postgres
# POSTGRES_PASSWORD=postgres
# POSTGRES_SERVER=localhost
# POSTGRES_PORT=5432
# POSTGRES_DB=carting
```

5. Set up PostgreSQL:

```bash
# Create database
createdb carting

# Or with psql
psql -U postgres -c "CREATE DATABASE carting"
```

## Running the Application

### Local Development

Run the application with:

```bash
python main.py
```

Or with uvicorn directly:

```bash
uvicorn src.app:app --reload
```

The API will be available at http://localhost:8000

### Using Docker

Build and run the application using Docker Compose:

```bash
docker-compose up --build
```

## API Documentation

Once the application is running, you can access:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

### Version Control

The project includes a `.gitignore` file that excludes:

- Python build artifacts and cache files
- Virtual environments
- Environment variables and local settings
- IDE-specific files
- Log files and databases
- Test coverage reports
- Package manager files

### Adding New Features

To add a new model:

1. Create a model in `src/models.py`
2. Create schemas in `src/schemas/`
3. Create services in `src/services/`
4. Create an endpoint in `src/api/endpoints/`
5. Include the router in `src/app.py`
6. Create database migrations using Alembic:
   ```bash
   alembic revision --autogenerate -m "Add new model"
   alembic upgrade head
   ```

### Testing

Run tests with:

```bash
pytest
```

For test coverage:

```bash
pytest --cov=src
```

### Code Quality

Before committing, ensure:

1. All tests pass
2. Code is formatted according to PEP 8
3. Type hints are properly used
4. Documentation is updated
5. No sensitive information is included in commits
