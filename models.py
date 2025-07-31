from app import db
from datetime import datetime

class GameStats(db.Model):
    """Store statistics for individual games"""
    __tablename__ = 'game_stats'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(32), nullable=False)
    difficulty = db.Column(db.String(10), nullable=False)
    mode = db.Column(db.String(20), nullable=False, default='quick_play')
    player_score = db.Column(db.Integer, default=0)
    ai_score = db.Column(db.Integer, default=0)
    winner = db.Column(db.String(10))  # 'player', 'ai', or 'tie'
    duration = db.Column(db.Integer, default=0)  # game duration in seconds
    hints_used = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<GameStats {self.session_id}: {self.winner}>'

class PlayerStats(db.Model):
    """Store aggregated player statistics"""
    __tablename__ = 'player_stats'
    
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String(16), unique=True, nullable=False)
    total_games = db.Column(db.Integer, default=0)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    ties = db.Column(db.Integer, default=0)
    total_score = db.Column(db.Integer, default=0)
    best_streak = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def win_rate(self):
        if self.total_games == 0:
            return 0
        return round((self.wins / self.total_games) * 100, 1)
    
    @property
    def average_score(self):
        if self.total_games == 0:
            return 0
        return round(self.total_score / self.total_games, 1)
    
    def __repr__(self):
        return f'<PlayerStats {self.player_id}: {self.wins}W-{self.losses}L-{self.ties}T>'
