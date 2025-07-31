import random

class CrosswordPuzzleManager:
    """Manages crossword puzzles with different difficulty levels"""
    
    def __init__(self):
        self.puzzles = {
            "easy": [
                {
                    "title": "Animals & Colors",
                    "size": 8,
                    "clues": [
                        {"id": 1, "clue": "Man's best friend", "answer": "DOG", "direction": "across", "position": [1, 2], "points": 5},
                        {"id": 2, "clue": "Feline pet", "answer": "CAT", "direction": "down", "position": [0, 4], "points": 5},
                        {"id": 3, "clue": "Color of the sun", "answer": "YELLOW", "direction": "across", "position": [3, 1], "points": 8},
                        {"id": 4, "clue": "Ocean mammal", "answer": "WHALE", "direction": "down", "position": [2, 6], "points": 7},
                        {"id": 5, "clue": "Flying insect", "answer": "BEE", "direction": "across", "position": [5, 3], "points": 5},
                        {"id": 6, "clue": "Color of grass", "answer": "GREEN", "direction": "down", "position": [1, 0], "points": 7},
                        {"id": 7, "clue": "Large grey animal", "answer": "ELEPHANT", "direction": "across", "position": [0, 0], "points": 10},
                        {"id": 8, "clue": "King of jungle", "answer": "LION", "direction": "down", "position": [4, 2], "points": 6}
                    ]
                },
                {
                    "title": "Food & Drinks",
                    "size": 8,
                    "clues": [
                        {"id": 9, "clue": "Red fruit", "answer": "APPLE", "direction": "across", "position": [1, 1], "points": 6},
                        {"id": 10, "clue": "Yellow fruit", "answer": "BANANA", "direction": "down", "position": [0, 3], "points": 8},
                        {"id": 11, "clue": "White liquid", "answer": "MILK", "direction": "across", "position": [3, 2], "points": 5},
                        {"id": 12, "clue": "Morning beverage", "answer": "COFFEE", "direction": "down", "position": [2, 6], "points": 8},
                        {"id": 13, "clue": "Italian dish", "answer": "PIZZA", "direction": "across", "position": [5, 0], "points": 7},
                        {"id": 14, "clue": "Sweet treat", "answer": "CAKE", "direction": "down", "position": [4, 4], "points": 6},
                        {"id": 15, "clue": "Orange vegetable", "answer": "CARROT", "direction": "across", "position": [0, 0], "points": 8},
                        {"id": 16, "clue": "H2O", "answer": "WATER", "direction": "down", "position": [1, 7], "points": 6}
                    ]
                }
            ],
            "medium": [
                {
                    "title": "Science & Nature",
                    "size": 10,
                    "clues": [
                        {"id": 17, "clue": "Study of stars", "answer": "ASTRONOMY", "direction": "across", "position": [0, 0], "points": 12},
                        {"id": 18, "clue": "Chemical element H", "answer": "HYDROGEN", "direction": "down", "position": [1, 5], "points": 10},
                        {"id": 19, "clue": "Planet closest to sun", "answer": "MERCURY", "direction": "across", "position": [3, 2], "points": 9},
                        {"id": 20, "clue": "Process of evolution", "answer": "MUTATION", "direction": "down", "position": [2, 8], "points": 10},
                        {"id": 21, "clue": "Earth's satellite", "answer": "MOON", "direction": "across", "position": [6, 4], "points": 6},
                        {"id": 22, "clue": "Photosynthesis gas", "answer": "OXYGEN", "direction": "down", "position": [4, 1], "points": 8},
                        {"id": 23, "clue": "Speed of light unit", "answer": "METERS", "direction": "across", "position": [8, 2], "points": 8},
                        {"id": 24, "clue": "DNA building block", "answer": "NUCLEOTIDE", "direction": "down", "position": [0, 9], "points": 15}
                    ]
                },
                {
                    "title": "History & Geography",
                    "size": 10,
                    "clues": [
                        {"id": 25, "clue": "Ancient Egyptian ruler", "answer": "PHARAOH", "direction": "across", "position": [1, 2], "points": 9},
                        {"id": 26, "clue": "Longest river", "answer": "NILE", "direction": "down", "position": [0, 4], "points": 6},
                        {"id": 27, "clue": "Roman empire capital", "answer": "ROME", "direction": "across", "position": [4, 5], "points": 6},
                        {"id": 28, "clue": "Tallest mountain", "answer": "EVEREST", "direction": "down", "position": [2, 0], "points": 9},
                        {"id": 29, "clue": "Largest continent", "answer": "ASIA", "direction": "across", "position": [7, 3], "points": 6},
                        {"id": 30, "clue": "French revolution year", "answer": "SEVENTEEN", "direction": "down", "position": [3, 8], "points": 12},
                        {"id": 31, "clue": "First man on moon", "answer": "ARMSTRONG", "direction": "across", "position": [0, 0], "points": 12},
                        {"id": 32, "clue": "Great wall country", "answer": "CHINA", "direction": "down", "position": [5, 6], "points": 7}
                    ]
                }
            ],
            "hard": [
                {
                    "title": "Advanced Science",
                    "size": 12,
                    "clues": [
                        {"id": 33, "clue": "Quantum physics principle", "answer": "UNCERTAINTY", "direction": "across", "position": [0, 0], "points": 18},
                        {"id": 34, "clue": "Einstein's theory", "answer": "RELATIVITY", "direction": "down", "position": [2, 5], "points": 15},
                        {"id": 35, "clue": "Subatomic particle", "answer": "NEUTRINO", "direction": "across", "position": [4, 2], "points": 12},
                        {"id": 36, "clue": "DNA replication enzyme", "answer": "POLYMERASE", "direction": "down", "position": [1, 9], "points": 15},
                        {"id": 37, "clue": "Mathematical constant", "answer": "FIBONACCI", "direction": "across", "position": [7, 1], "points": 12},
                        {"id": 38, "clue": "Cellular powerhouse", "answer": "MITOCHONDRIA", "direction": "down", "position": [3, 11], "points": 20},
                        {"id": 39, "clue": "Periodic table creator", "answer": "MENDELEEV", "direction": "across", "position": [10, 0], "points": 15},
                        {"id": 40, "clue": "Light particle", "answer": "PHOTON", "direction": "down", "position": [6, 7], "points": 10}
                    ]
                },
                {
                    "title": "Literature & Philosophy",
                    "size": 12,
                    "clues": [
                        {"id": 41, "clue": "Hamlet's author", "answer": "SHAKESPEARE", "direction": "across", "position": [0, 0], "points": 18},
                        {"id": 42, "clue": "Greek philosopher", "answer": "ARISTOTLE", "direction": "down", "position": [2, 4], "points": 12},
                        {"id": 43, "clue": "Epic poem by Homer", "answer": "ODYSSEY", "direction": "across", "position": [5, 3], "points": 10},
                        {"id": 44, "clue": "Existentialist writer", "answer": "SARTRE", "direction": "down", "position": [1, 8], "points": 10},
                        {"id": 45, "clue": "Russian novelist", "answer": "DOSTOEVSKY", "direction": "across", "position": [8, 1], "points": 15},
                        {"id": 46, "clue": "Utopian novel author", "answer": "ORWELL", "direction": "down", "position": [4, 10], "points": 10},
                        {"id": 47, "clue": "Medieval epic", "answer": "BEOWULF", "direction": "across", "position": [11, 2], "points": 12},
                        {"id": 48, "clue": "Philosophical method", "answer": "DIALECTIC", "direction": "down", "position": [6, 6], "points": 12}
                    ]
                }
            ]
        }
    
    def get_puzzle(self, difficulty="medium"):
        """Get a random puzzle of specified difficulty"""
        if difficulty not in self.puzzles:
            difficulty = "medium"
        
        puzzle_list = self.puzzles[difficulty]
        if not puzzle_list:
            return None
            
        return random.choice(puzzle_list)
    
    def get_all_difficulties(self):
        """Get list of available difficulty levels"""
        return list(self.puzzles.keys())
    
    def get_puzzle_count(self, difficulty):
        """Get number of puzzles for a difficulty level"""
        return len(self.puzzles.get(difficulty, []))
