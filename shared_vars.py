import os
from pony.orm import Database

db = Database()

database_url = os.getenv("DATABASE_URL")
if database_url:
    # Render gives DATABASE_URL like: postgres://user:pass@host:port/dbname
    db.bind(provider='postgres', dsn=database_url)
else:
    # Local fallback
   db.bind(provider='sqlite', filename=os.getenv('UNO_DB', 'uno.sqlite3'), create_db=True)

#shared_vars.py

class GameManager:
    def __init__(self):
        self.active_games = {}  # chat_id -> game state
        self.players = {}       # user_id -> player data

    def start_game(self, chat_id):
        if chat_id not in self.active_games:
            self.active_games[chat_id] = {
                "players": [],
                "deck": [],
                "discard": [],
                "turn": 0,
                "direction": 1
            }
        return self.active_games[chat_id]

    def add_player(self, chat_id, user_id):
        game = self.active_games.get(chat_id)
        if game:
            if user_id not in game["players"]:
                game["players"].append(user_id)

    def next_turn(self, chat_id):
        game = self.active_games.get(chat_id)
        if game:
            game["turn"] = (game["turn"] + game["direction"]) % len(game["players"])
            return game["players"][game["turn"]]
        return None


# ✅ export gm as a global instance
gm = GameManager()
