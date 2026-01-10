# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Django web application that validates "World XI" fantasy football team selections. Users must pick 11 players where no two share the same country or have played for the same club. The app scrapes Transfermarkt for player data.

Live site: https://www.schubmann.dev/

## Common Commands

### Development
```bash
pipenv install --dev          # Install dependencies
python manage.py runserver    # Run dev server
daphne -b 0.0.0.0 -p 8000 footy_world_xi_validator.asgi:application  # ASGI server
```

### Testing
```bash
pytest                        # Run all tests
pytest footy_validator/tests/logic/test_squad_validation.py  # Single test file
pytest -k "test_name"         # Run tests matching pattern
```

### Code Quality (run via pre-commit)
```bash
pre-commit run --all-files    # Run all linters
black .                       # Format code
mypy .                        # Type checking
```

### Docker
```bash
docker-compose up                              # Development
docker-compose -f docker-compose.prod.yml up   # Production
```

## Architecture

### Tech Stack
- **Backend:** Django 4.1.2 with Django Configurations (environment-based settings)
- **Frontend:** Django templates + HTMX for dynamic interactions
- **Database:** PostgreSQL
- **Server:** Daphne (ASGI) or Gunicorn (WSGI on Heroku)
- **External Data:** Transfermarkt web scraping via BeautifulSoup4

### Key Directories
- `footy_validator/` - Main application with models, views, and business logic
- `footy_validator/logic/` - Core business logic (squad validation, Transfermarkt scraping)
- `footy_validator/repositories.py` - Data access layer using repository pattern
- `footy_validator/dataclasses.py` - Business logic dataclasses (separate from ORM)
- `components/` - Reusable django-components (e.g., team_view)
- `templates/partials/` - HTMX partial templates
- `footy_world_xi_validator/settings.py` - Contains Dev, Staging, Prod configuration classes

### Data Flow
1. User searches for players via HTMX partial views (`partials.py`)
2. Player data fetched from Transfermarkt (`logic/get_player_from_transfermarkt.py`)
3. Squad validation rules applied (`logic/squad_validation.py`)
4. Results rendered via django-components and HTMX partials

### Models
- `FootballPlayer` - Player with nationality and club history
- `NationalTeam`, `ClubTeam` - Team references
- `TemporaryUserSubmission`, `UserSubmission` - User squad selections

## Testing

Tests use pytest-django with factory_boy for model factories. Test fixtures for Transfermarkt HTML responses are in `footy_validator/tests/fixtures.py`.

Configuration: `pytest.ini`, `conftest.py` at project root and in `footy_validator/tests/`

## Environment Configuration

Uses django-configurations with three settings classes: `Dev`, `Staging`, `Prod`. Environment variables loaded from `.env.*` files. Set `DJANGO_CONFIGURATION` to select environment.
