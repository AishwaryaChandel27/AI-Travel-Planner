# AI Travel Planner

## Overview

This is a production-ready Flask-based web application that provides AI-powered travel planning services. The application uses Google Gemini AI to generate personalized destination recommendations and detailed travel itineraries based on user preferences. It includes a comprehensive mock booking system for flights, hotels, and activities, with a session-based workflow that guides users through preference collection, itinerary generation, and booking management.

## Recent Changes (July 14, 2025)

✓ Fixed circular import issues in application structure
✓ Created comprehensive README.md with GitHub-ready documentation
✓ Added proper error handling templates (404.html, 500.html)
✓ Created demo script for testing AI features
✓ Added LICENSE and .gitignore files for open source distribution
✓ Improved navigation icons and user experience
✓ Enhanced error handling and robustness
✓ **NEW: Country-specific budget system with realistic local currencies**
✓ **NEW: Dynamic currency conversion and budget ranges (₹, ¥, £, €, $, etc.)**
✓ **NEW: Destination image generation with SVG graphics**
✓ **NEW: Enhanced AI recommendations with country-specific context**
✓ Application is now fully functional and deployment-ready

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: HTML templates with Bootstrap 5 (dark theme)
- **Styling**: Custom CSS with travel-themed design elements
- **JavaScript**: Vanilla JavaScript for form validation and interactive features
- **Template Engine**: Jinja2 templates with Flask
- **UI Components**: Bootstrap components with Font Awesome icons

### Backend Architecture
- **Framework**: Flask web application with session management
- **Database**: SQLAlchemy with SQLite (development) or PostgreSQL (production)
- **AI Integration**: Google Gemini API for travel recommendations and itinerary generation
- **Session Management**: Flask sessions with UUID-based session IDs
- **Service Layer**: Separate service classes for business logic

### Data Storage
- **Primary Database**: SQLite for development, configurable for PostgreSQL in production
- **ORM**: SQLAlchemy with declarative base model
- **Session Storage**: Flask built-in session management
- **JSON Storage**: Complex data structures stored as JSON in database columns

## Key Components

### Models (models.py)
- **TravelPreference**: Stores user travel preferences including budget, dates, interests, and group size
- **Itinerary**: Contains generated travel plans with activities, budget breakdowns, and AI recommendations
- **Booking**: Manages mock booking records for flights, hotels, and activities

### AI Service (gemini.py)
- **TravelRecommendation**: Pydantic model for structured destination recommendations
- **ItineraryPlan**: Pydantic model for detailed travel itineraries
- **Gemini Integration**: Uses Google Gemini API for generating travel content

### Travel Service (travel_service.py)
- **Mock Booking System**: Simulates flight, hotel, and activity searches
- **Data Generation**: Creates realistic travel options with pricing and availability
- **Search Functionality**: Provides search interfaces for different travel services

### Route Handlers (routes.py)
- **Preference Collection**: Multi-step form for gathering user travel preferences
- **Itinerary Generation**: AI-powered travel plan creation
- **Booking Management**: Mock booking system for travel services
- **Session Management**: User session handling and data persistence

## Data Flow

1. **User Input**: Users provide travel preferences through web forms
2. **Preference Storage**: Data is stored in SQLite database with session tracking
3. **AI Processing**: Gemini AI generates destination recommendations and itineraries
4. **Itinerary Creation**: Structured travel plans are created and stored
5. **Booking Simulation**: Mock booking system provides realistic travel options
6. **Session Management**: User progress is tracked throughout the planning process

## External Dependencies

### Core Dependencies
- **Flask**: Web framework and application server
- **SQLAlchemy**: Database ORM and connection management
- **Google Gemini**: AI service for travel recommendations
- **Bootstrap 5**: Frontend UI framework
- **Font Awesome**: Icon library for user interface

### Development Dependencies
- **Werkzeug**: WSGI utilities and development server
- **Pydantic**: Data validation and serialization
- **UUID**: Session identifier generation

## Deployment Strategy

### Environment Configuration
- **Database URL**: Configurable via `DATABASE_URL` environment variable
- **Session Secret**: Configurable via `SESSION_SECRET` environment variable
- **Gemini API Key**: Required via `GEMINI_API_KEY` environment variable

### Production Considerations
- **Database**: Designed to work with PostgreSQL in production
- **Proxy Support**: Includes ProxyFix middleware for deployment behind reverse proxies
- **Connection Pooling**: Configured with pool recycling and health checks
- **Static Assets**: CSS and JavaScript files served through Flask static file handling

### Development Setup
- **Local Development**: Uses SQLite database for easy setup
- **Debug Mode**: Configurable debug mode for development
- **Port Configuration**: Runs on port 5000 with host binding to 0.0.0.0

The application follows a traditional MVC pattern with clear separation of concerns between data models, business logic, and presentation layers. The AI integration provides the core value proposition while the mock booking system demonstrates the complete travel planning workflow.