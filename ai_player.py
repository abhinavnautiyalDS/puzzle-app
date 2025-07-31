import random
import time

class AIPlayer:
    """AI opponent for crossword battle game"""
    
    def __init__(self):
        self.difficulty_settings = {
            "easy": {
                "accuracy": 0.7,  # 70% chance to get answer right
                "thinking_time": 3,
                "prefer_short": True
            },
            "medium": {
                "accuracy": 0.85,  # 85% chance to get answer right
                "thinking_time": 2,
                "prefer_short": False
            },
            "hard": {
                "accuracy": 0.95,  # 95% chance to get answer right
                "thinking_time": 1,
                "prefer_short": False
            }
        }
    
    def select_clue(self, available_clues, difficulty="medium"):
        """AI selects which clue to answer based on difficulty and strategy"""
        if not available_clues:
            return None
        
        settings = self.difficulty_settings.get(difficulty, self.difficulty_settings["medium"])
        
        # Strategy: prefer shorter words on easy difficulty
        if settings["prefer_short"]:
            # Sort by answer length, prefer shorter ones
            sorted_clues = sorted(available_clues, key=lambda x: len(x.get("answer", "")))
            # Select from the first half (shorter answers)
            selection_pool = sorted_clues[:max(1, len(sorted_clues) // 2)]
        else:
            # On harder difficulties, prefer higher point values
            sorted_clues = sorted(available_clues, key=lambda x: x.get("points", 10), reverse=True)
            # Select from the top third (higher points)
            selection_pool = sorted_clues[:max(1, len(sorted_clues) // 3)]
        
        # Add some randomness
        selected_clue = random.choice(selection_pool)
        
        # Simulate AI "thinking" - this happens in a separate thread
        thinking_time = settings["thinking_time"] + random.uniform(-0.5, 0.5)
        time.sleep(max(0.5, thinking_time))
        
        return selected_clue
    
    def should_answer_correctly(self, difficulty="medium"):
        """Determine if AI should answer correctly based on difficulty"""
        settings = self.difficulty_settings.get(difficulty, self.difficulty_settings["medium"])
        return random.random() < settings["accuracy"]
    
    def get_thinking_time(self, difficulty="medium"):
        """Get AI thinking time for the difficulty level"""
        settings = self.difficulty_settings.get(difficulty, self.difficulty_settings["medium"])
        base_time = settings["thinking_time"]
        # Add some variation
        return base_time + random.uniform(-0.5, 0.5)
    
    def calculate_strategy_score(self, clue, game_state):
        """Calculate strategic value of answering a particular clue"""
        base_score = clue.get("points", 10)
        
        # Bonus for longer words (more impressive)
        length_bonus = len(clue.get("answer", "")) * 2
        
        # Bonus for crossing words (strategic positioning)
        position_bonus = 5 if clue.get("direction") == "across" else 3
        
        return base_score + length_bonus + position_bonus
    
    def get_difficulty_stats(self):
        """Return AI performance statistics by difficulty"""
        return {
            "easy": {
                "win_rate": 30,
                "avg_score": 45,
                "avg_time": 3.2
            },
            "medium": {
                "win_rate": 50,
                "avg_score": 72,
                "avg_time": 2.1
            },
            "hard": {
                "win_rate": 70,
                "avg_score": 95,
                "avg_time": 1.3
            }
        }
