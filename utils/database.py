import sqlite3

class Database:
    def __init__(self, db_name="social_media.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT,
            message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")
        self.conn.commit()

    def insert_log(self, platform, message):
        self.cursor.execute("INSERT INTO logs (platform, message) VALUES (?, ?)", (platform, message))
        self.conn.commit()
