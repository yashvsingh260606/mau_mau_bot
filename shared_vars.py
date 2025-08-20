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
