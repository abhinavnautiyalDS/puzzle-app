# Crossword Battle Game

A real-time crossword battle game where players compete against AI opponents in turn-based puzzle solving.

## Features

- **Modern Interface**: Sleek card-based design with dark theme
- **Difficulty Levels**: Easy, Medium, and Hard AI opponents
- **Game Modes**: Quick Play (race to 100 points) and Tournament (complete all clues)
- **Real-time Gameplay**: Turn-based mechanics with visual feedback
- **Score Tracking**: Persistent statistics and game history
- **Responsive Design**: Works on desktop and mobile devices

## Deployment

### Deploy to Render

1. **Fork or clone this repository**
2. **Connect to Render**:
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New" > "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect the `render.yaml` file

3. **Database Setup**:
   - A PostgreSQL database will be automatically created
   - Environment variables will be automatically configured

4. **Deploy**:
   - Click "Apply" to deploy
   - Your app will be available at `https://your-app-name.onrender.com`

### Manual Deployment

If you prefer manual deployment:

1. **Create a Web Service**:
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn --bind 0.0.0.0:$PORT --reuse-port main:app`

2. **Create a PostgreSQL Database**:
   - Add the connection string as `DATABASE_URL` environment variable

3. **Add Environment Variables**:
   - `SESSION_SECRET`: Generate a random secret key
   - `DATABASE_URL`: PostgreSQL connection string

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables**:
   ```bash
   export DATABASE_URL="sqlite:///crossword.db"
   export SESSION_SECRET="your-secret-key"
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

4. **Open in browser**:
   - Visit `http://localhost:5000`

## Game Rules

- **Objective**: Be the first to reach 100 points (Quick Play) or complete all clues (Tournament)
- **Scoring**: Each clue has point values based on difficulty and word length
- **Hints**: You get 3 hints per game - use them wisely!
- **AI Difficulty**:
  - **Easy**: 70% accuracy, prefers short words, 3-second delay
  - **Medium**: 85% accuracy, balanced strategy, 2-second delay  
  - **Hard**: 95% accuracy, targets high-point clues, 1-second delay

## Technology Stack

- **Backend**: Flask, SQLAlchemy, PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5 with custom dark theme
- **Icons**: Font Awesome
- **Deployment**: Gunicorn, Render Platform

## License

MIT License - feel free to use this project for your own purposes.