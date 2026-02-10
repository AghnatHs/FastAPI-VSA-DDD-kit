# FastAPI VSA-DDD Template (WORK IN PROGRESS)

A FastAPI template implementing Vertical Slice Architecture (VSA) and Domain-Driven Design (DDD) approach with async PostgreSQL support. Purposely for System Analysis and Design courses (KOM1337) so it may need some changes for another use.

check out my other template : [Nest TS Starter Kit](https://github.com/AghnatHs/nest-core-kit)

!! Not fully implementing DDD

### Project Structure

```
├── src/
│   ├── app.py                 # FastAPI application entry point
│   ├── core/                  # Core infrastructure
│   │   ├── config.py          # Application configuration
│   │   └── db.py              # Database setup and session management
│   ├── domain/                # Domain models (business entities)
│   │   └── user.py            # User domain model
│   ├── features/              # Feature slices (VSA)
│   └── infrastructure/        # Infrastructure layer
│       └── tables/            # SQLAlchemy table mappings
│           ├── user_table.py  # User table ORM
│           └── __init__.py
├── alembic/                   # Database migrations
│   ├── env.py                 # Alembic environment config
│   └── versions/              # Migration scripts
├── main.py                    # Application entry point
├── pyproject.toml             # Project dependencies
├── requirements.txt           # Pip dependencies
└── alembic.ini               # Alembic configuration
```

## Features

- **Database Migrations**: Alembic integration for schema versioning
- **Domain Models**: Rich domain models with business logic
- **Vertical Slice**: Separate by business language / domain
- **Environment Config**: `.env` based configuration
- **Code Quality**: Pre-commit hooks with Black and Ruff
- **Type Safety**: Full type hints support

## 📋 Prerequisites

- Python 3.13.11+
- PostgreSQL 17+
- Git

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd fastapi-vsa-ddd
   ```

2. **Venv and its dependencies**

   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync

   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

## Configuration

Edit `.env` file with your settings:

```env
APP_ENV=development
PORT=9000

DB_HOST=localhost
DB_PORT=5432
DB_NAME=app_db
DB_USER=postgres
DB_PASSWORD=postgres
```

Configuration is managed in [`src/core/config.py`](src/core/config.py).

## Database Setup

2. **Run migrations**

   ```bash
   alembic upgrade head
   ```

3. **Create new migration** (after model changes)
   ```bash
   alembic revision --autogenerate -m "description"
   alembic upgrade head
   ```

## Running the Application

**Development mode (auto reload)**:

```bash
python main.py
```

**Production mode**:

```bash
uvicorn src.app:app --host 0.0.0.0 --port 9000
```

The API will be available at `http://localhost:9000`

## Code Style

- **Black**: Code formatting
- **Ruff**: Fast Python linter
- **Pre-commit**: Automated code quality checks

Run manually:

```bash
black .
ruff check --fix
```

## Testing

```bash
pytest
```
