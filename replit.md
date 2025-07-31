# Crossword Battle Game

## Overview

This is a real-time crossword battle game where players compete against an AI opponent to solve crossword puzzles. The application is built with Flask as the backend, SQLAlchemy for database operations, and a web-based frontend with real-time gameplay features.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask web application with SQLAlchemy ORM
- **Database**: SQLite (development) with support for PostgreSQL via DATABASE_URL environment variable
- **Session Management**: Flask sessions with in-memory game state storage
- **AI Component**: Custom AI player with configurable difficulty levels
- **Real-time Features**: Threading for AI turn simulation and game state polling

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Bootstrap 5 for responsive UI
- **JavaScript**: Vanilla JavaScript with Bootstrap components for modals and interactions
- **Styling**: Custom CSS with Bootstrap dark theme and Font Awesome icons
- **Real-time Updates**: Client-side polling for game state changes

### Data Storage
- **Primary Database**: SQLAlchemy with support for multiple database backends
- **Game Sessions**: In-memory storage (suitable for single-instance deployment)
- **Statistics Tracking**: Persistent storage for game and player statistics

## Key Components

### 1. Game Logic (`crossword_data.py`)
- **Purpose**: Manages crossword puzzles with different difficulty levels
- **Features**: Hierarchical puzzle structure with easy/medium/hard categories
- **Data Structure**: Clues with positions, directions, answers, and point values

### 2. AI Player (`ai_player.py`)
- **Purpose**: Provides intelligent AI opponent with configurable behavior
- **Difficulty Levels**: Easy (70% accuracy), Medium (85% accuracy), Hard (95% accuracy)
- **Strategy**: Difficulty-based clue selection (short words for easy, high points for hard)
- **Timing**: Simulated thinking time with randomization

### 3. Database Models (`models.py`)
- **GameStats**: Individual game records with scores, duration, and outcome
- **PlayerStats**: Aggregated player statistics with win rates and streaks
- **Features**: Calculated properties for win rates and average scores

### 4. Main Application (`app.py`)
- **Flask Setup**: Application factory pattern with configuration management
- **Database Configuration**: Environment-based database URL with connection pooling
- **Global Managers**: Singleton instances for puzzle and AI management
- **Session Handling**: Game session class for state management

### 5. Frontend Components
- **Base Template**: Responsive layout with navigation and modal containers
- **Game Interface**: Dynamic grid display with real-time score updates
- **JavaScript Game Engine**: Class-based architecture for game state management

## Data Flow

### Game Initialization
1. Player selects difficulty and game mode through web form
2. Flask creates new GameSession with unique session ID
3. CrosswordPuzzleManager provides puzzle data based on difficulty
4. Game state stored in memory with session mapping

### Gameplay Loop
1. Player submits answer through web interface
2. Server validates answer and updates scores
3. AI player selects and attempts clue based on difficulty settings
4. Game state updated with both player and AI actions
5. Frontend polls for state changes and updates UI

### Game Completion
1. Win condition checked after each turn (score threshold or grid completion)
2. Final statistics calculated and stored in database
3. Player statistics updated with aggregated data
4. Game session cleaned up from memory

## External Dependencies

### Python Packages
- **Flask**: Web framework and routing
- **SQLAlchemy**: Database ORM and migrations
- **Werkzeug**: WSGI utilities and proxy handling

### Frontend Libraries
- **Bootstrap 5**: UI framework with dark theme support
- **Font Awesome**: Icon library for enhanced UI
- **Vanilla JavaScript**: No additional frameworks required

### Runtime Dependencies
- **Threading**: For AI turn simulation
- **Random**: For AI decision making and puzzle selection
- **Time/Datetime**: For game timing and statistics

## Deployment Strategy

### Environment Configuration
- **DATABASE_URL**: Supports SQLite (default) and PostgreSQL
- **SESSION_SECRET**: Configurable session security key
- **Debug Mode**: Controlled via Flask debug flag

### Database Strategy
- **Development**: SQLite with file-based storage
- **Production**: PostgreSQL support via environment variable
- **Migration Path**: SQLAlchemy models support database upgrades

### Scalability Considerations
- **Session Storage**: Currently in-memory (requires Redis for multi-instance)
- **AI Processing**: Threaded but single-instance (requires message queue for scaling)
- **Database**: Connection pooling configured for production use

### Production Readiness
- **Security**: ProxyFix middleware for reverse proxy deployment
- **Logging**: Configurable logging levels
- **Error Handling**: Database connection retry logic
- **Performance**: Connection pooling and pre-ping validation