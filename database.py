from pony.orm import Database, PrimaryKey, Required, Set
from config import DATABASE_URL

db = Database()


class GameSession(db.Entity):
    id = PrimaryKey(int, auto=True)
    chat_id = Required(int)
    status = Required(str)   # e.g. "waiting", "active", "finished"
    players = Set("Player")


class Player(db.Entity):
    id = PrimaryKey(int, auto=True)
    user_id = Required(int)      # Telegram user id
    username = Required(str)
    game = Required(GameSession)


class UserSetting(db.Entity):
    id = PrimaryKey(int, auto=True)
    user_id = Required(int, unique=True)
    language = Required(str, default="en")
    notifications = Required(bool, default=True)


db.bind(provider="postgres", dsn=DATABASE_URL)
db.generate_mapping(create_tables=True)
