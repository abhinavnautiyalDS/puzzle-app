# Deployment Guide

## Environment Configuration

### 1. Environment Files

The project includes several environment configuration files:

- **`.env.example`** - Template showing all required environment variables
- **`.env.local`** - Pre-configured for local development with SQLite
- **`.env.production`** - Template for production deployment

### 2. Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `postgresql://user:pass@host:5432/db` |
| `SESSION_SECRET` | Secret key for session security | `your-random-secret-key` |
| `FLASK_ENV` | Flask environment mode | `production` or `development` |
| `FLASK_DEBUG` | Enable/disable debug mode | `False` for production |
| `LOG_LEVEL` | Logging verbosity | `INFO` for production |

## Deployment Options

### Option 1: Render (Recommended) - Zero Configuration

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy to Render**:
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New" > "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml`
   - Click "Apply" to deploy

3. **Automatic Setup**:
   - ✅ PostgreSQL database created automatically
   - ✅ Environment variables configured automatically
   - ✅ SSL certificate generated
   - ✅ Domain provided: `https://your-app.onrender.com`

### Option 2: Manual Render Deployment

1. **Create Web Service**:
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn --bind 0.0.0.0:$PORT --reuse-port main:app`

2. **Create PostgreSQL Database**:
   - Add a PostgreSQL database service
   - Copy the connection string

3. **Set Environment Variables**:
   ```
   DATABASE_URL=postgresql://...
   SESSION_SECRET=your-secret-key
   FLASK_ENV=production
   FLASK_DEBUG=False
   ```

### Option 3: Heroku Deployment

1. **Install Heroku CLI** and login:
   ```bash
   heroku login
   ```

2. **Create Heroku app**:
   ```bash
   heroku create your-app-name
   ```

3. **Add PostgreSQL**:
   ```bash
   heroku addons:create heroku-postgresql:mini
   ```

4. **Set environment variables**:
   ```bash
   heroku config:set SESSION_SECRET=your-secret-key
   heroku config:set FLASK_ENV=production
   heroku config:set FLASK_DEBUG=False
   ```

5. **Deploy**:
   ```bash
   git push heroku main
   ```

### Option 4: Railway Deployment

1. **Connect to Railway**:
   - Go to [Railway](https://railway.app/)
   - Connect your GitHub repository

2. **Add PostgreSQL**:
   - Click "Add Service" > "Database" > "PostgreSQL"

3. **Configure Variables**:
   - `DATABASE_URL` (automatically set by Railway)
   - `SESSION_SECRET=your-secret-key`
   - `FLASK_ENV=production`

## Local Development

### Quick Start

1. **Clone and setup**:
   ```bash
   git clone your-repo
   cd crossword-battle-game
   pip install -r requirements.txt
   ```

2. **Use local environment**:
   ```bash
   cp .env.local .env
   # Edit .env if needed
   ```

3. **Run locally**:
   ```bash
   python main.py
   ```

4. **Access app**:
   - Open `http://localhost:5000`

### Custom Configuration

1. **Copy environment template**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your values**:
   ```bash
   DATABASE_URL=sqlite:///crossword.db  # or PostgreSQL URL
   SESSION_SECRET=your-secret-key
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```

## Database Setup

### PostgreSQL (Production)

The application automatically creates all required database tables on first run. No manual database setup required.

**Tables created automatically**:
- `game_stats` - Individual game records
- `player_stats` - Aggregated player statistics

### SQLite (Development)

For local development, SQLite is used by default. The database file `crossword.db` will be created automatically in the project root.

## Security Considerations

### Session Secret

**Important**: Always use a strong, random session secret in production:

```python
# Generate a secure secret key
import secrets
secrets.token_urlsafe(32)
```

### Environment Variables

- Never commit `.env` files to version control
- Use secure, randomly generated secrets
- Keep database credentials secure
- Use environment-specific configurations

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Check `DATABASE_URL` format
   - Verify database server is running
   - Check network connectivity

2. **Session Errors**:
   - Ensure `SESSION_SECRET` is set
   - Use a strong secret key (not the default)

3. **Static Files Not Loading**:
   - Check file paths in templates
   - Verify static file serving configuration

4. **Port Issues**:
   - Use `0.0.0.0:$PORT` for cloud deployment
   - Use `127.0.0.1:5000` for local development

### Logs and Debugging

- Check application logs in your deployment platform
- Set `LOG_LEVEL=DEBUG` for detailed logging
- Use `FLASK_DEBUG=True` only in development

## Monitoring

### Health Check Endpoint

The application includes a health check at `/health`:

```bash
curl https://your-app.com/health
# Returns: {"status": "healthy"}
```

### Database Health

Monitor database connectivity and performance through your hosting platform's dashboard.

## Scaling

### Horizontal Scaling

The application is stateless and can be scaled horizontally:
- Session data is stored in database
- No in-memory state dependencies
- Multiple instances can run simultaneously

### Database Scaling

For high traffic:
- Consider database connection pooling
- Monitor query performance
- Add database indexes if needed