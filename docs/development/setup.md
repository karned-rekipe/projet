# Development Setup

This guide provides instructions for setting up a development environment for the API Recipe service.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.12 or higher
- Git
- Docker (optional, for containerized development)
- Redis (for caching and session management)

## Clone the Repository

```bash
git clone https://github.com/karned-rekipe/api-recipe.git
cd api-recipe
```

## Virtual Environment

It's recommended to use a virtual environment for development:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

## Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

For development, you may also want to install additional packages:

```bash
pip install pytest pytest-cov black isort flake8
```

## Configuration

The API Recipe service uses environment variables for configuration. Create a `.env` file in the root directory with the following variables:

```
# API Configuration
PYTHONUNBUFFERED=True
WORKERS=1
API_NAME=api-recipe
API_TAG_NAME=recipes

# Keycloak Configuration
KEYCLOAK_HOST=
KEYCLOAK_REALM=
KEYCLOAK_CLIENT_ID=
KEYCLOAK_CLIENT_SECRET=

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=
```

## Database Setup

The API Recipe service uses Redis for caching and session management. Make sure Redis is running:

```bash
# Start Redis using Docker
docker run --name redis -p 6379:6379 -d redis

# Or if you have Redis installed locally
redis-server
```

## Running the Application

Start the application in development mode:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`.

## API Documentation

The API documentation is available at `http://localhost:8000/docs` when the application is running.

## Running Tests

Run the tests using pytest:

```bash
pytest
```

To generate a coverage report:

```bash
pytest --cov=.
```

## Code Formatting

Format your code using Black and isort:

```bash
black .
isort .
```

Check for linting issues:

```bash
flake8
```

## Debugging

For debugging, you can use the built-in debugger in your IDE or the Python debugger (pdb).

To use pdb, add the following line where you want to set a breakpoint:

```python
import pdb; pdb.set_trace()
```

## Documentation

The project documentation is built using MkDocs. To build and serve the documentation locally:

```bash
mkdocs serve
```

The documentation will be available at `http://localhost:8000`.
