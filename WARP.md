# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

The Personalized Career and Skills Advisor is a complete Flask-based web application that provides personalized career guidance and skills development recommendations. The application includes a full web interface, user authentication, skills assessments, career recommendations, and progress tracking.

## Architecture

### Core Components

- **Flask Web Application**: Complete web application with blueprints (`src/app.py`) serving both web pages and API endpoints
- **Database Models**: Comprehensive SQLAlchemy models for users, skills, careers, assessments, and recommendations (`src/models/__init__.py`)
- **Assessment Engine**: Intelligent skills assessment system with dynamic question generation (`src/services/assessment_engine.py`)
- **Recommendation Engine**: Machine learning-inspired career matching algorithm (`src/services/recommendation_engine.py`)
- **Authentication System**: Complete user registration, login, and profile management (`src/blueprints/auth.py`)
- **Web Interface**: Responsive Bootstrap-based frontend with interactive features (`src/templates/`, `src/static/`)
- **Configuration Management**: Environment-based settings with dataclass configuration (`config/settings.py`)
- **Modular Architecture**: Clean separation using Flask blueprints and service layers

### API Design

The application follows RESTful principles with these key endpoints:
- `GET /` - Application status and version info
- `GET /health` - Health check for monitoring
- `POST /api/skills/assess` - Skills assessment (placeholder implementation)
- `GET /api/career/recommendations` - Career recommendations with match scores

### Configuration Architecture

Uses dataclass-based configuration with environment-specific settings (Development, Production, Testing). The configuration supports:
- Database configuration (currently SQLite, prepared for scaling)
- API versioning and content limits
- Skills assessment parameters (timeout, max skills)
- Career recommendation filtering (min match score, max results)

### Data Model

The database schema includes these key entities:
- **User**: Authentication and profile information including skills, experience, and education
- **Skill**: Technical, soft, and industry-specific skills with descriptions and categories
- **Career**: Career paths with required skills, salary info, and growth potential
- **Assessment**: User skills assessments with responses and overall scores
- **CareerRecommendation**: Generated recommendations with match scores and skill gaps
- **ProgressEntry**: Tracking of user skill development over time

## Development Commands

### Setup and Installation
```bash
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
# Run the complete application
python run.py

# Or run directly from src
python src/app.py

# With environment variables
FLASK_ENV=development python src/app.py
```

### Testing
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_main.py

# Run specific test
pytest tests/test_main.py::test_health_check
```

### Code Quality
```bash
# Format code with Black
black src/ tests/ config/

# Lint with flake8
flake8 src/ tests/ config/

# Format and lint together
black src/ tests/ config/ && flake8 src/ tests/ config/
```

### Development Workflow
```bash
# Check application health
curl http://localhost:5000/health

# Test skills assessment endpoint
curl -X POST http://localhost:5000/api/skills/assess \
  -H "Content-Type: application/json" \
  -d '{"user_id": "test", "skills": ["Python", "Flask"]}'

# Get career recommendations
curl http://localhost:5000/api/career/recommendations
```

## Key Development Patterns

### Flask Application Structure
- Single-file application pattern for simplicity during early development
- JSON API responses with consistent error handling
- Environment-based configuration loading
- Structured logging throughout the application

### Testing Strategy
- Flask test client for API endpoint testing
- Pytest fixtures for test setup
- JSON response validation
- API contract testing for request/response structure

### Configuration Management
- Environment variable support for sensitive settings
- Default values for development convenience
- Dataclass-based type-safe configuration
- Environment-specific configuration classes

### Assessment Engine Design
- Dynamic question generation based on skill categories
- Question templates with skill-specific content insertion
- Comprehensive scoring system with 1-5 rating scale
- User skills tracking and progress monitoring
- Category-based insights and recommendations

### Recommendation Engine Design
- Weighted skill matching algorithm
- Profile-based bonus scoring (industry, experience, education)
- Gap analysis for skills development
- Personalized action recommendations
- Explanation generation for match scores

## Project Status

This is a fully functional web application with the following implemented features:
- Complete user authentication and profile management
- Dynamic skills assessment with 20+ question types across technical, soft, and industry-specific skills
- Intelligent career recommendation engine with match scoring and gap analysis
- Progress tracking and skill level management
- Responsive web interface with Bootstrap styling
- REST API endpoints for programmatic access
- SQLAlchemy database with comprehensive data models
- Sample data including 30+ skills, 12 career paths, and demo user

## Demo Credentials
- Username: `demo_user`
- Password: `demo123`

## Key Features
- **Skills Assessment**: 20-question comprehensive evaluation across multiple skill categories
- **Career Matching**: Algorithm analyzes skills against 12+ career paths with detailed explanations
- **Progress Tracking**: Monitor skill development over time with visual progress indicators
- **User Profiles**: Complete profile management with industry and experience tracking
- **Responsive Design**: Mobile-friendly interface that works across all device sizes