from binance import ThreadedWebsocketManager
from binance.client import Client

import sqlite3
from datetime import datetime

import threading
from config import APIKeys

class Database():

    def __init__(self, db_file = "data.db"):

        self.db_file = db_file
        self.lock = threading.Lock()

        self.api_keys = APIKeys
        self.api_key = self.api_keys.get("API_KEY")
        self.api_secret = self.api_keys.get("API_SECRET")
        self.client = Client(api_key=self.api_key, api_secret=self.api_secret)

        self.twm = ThreadedWebsocketManager()

        self._initialize_db()

    def _connect(self):

        return sqlite3.connect(database=self.db_file, check_same_thread=False)
    
    def _intialize_db(self):

        with self._connect() as conn:
            cursor = conn.cursor()

            cursor.executescript("""
                CREATE TABLE IF NOT EXISTS historical_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                timestamp INTEGER NOT NULL,
                open REAL NOT NULL,
                high REAL NOT NULL,
                low REAL NOT NULL,
                close REAL NOT NULL,
                volume REAL NOT NULL
                )
            """);
    
            conn.commit()

    def insert_data(self, symbol, timestamp, open_price, high_price, low_price, close_price, volume):

        with self.lock, self._connect as conn:
            cursor = conn.cursor()

            cursor.executescript("""
                INSERT INTO historical_data (symbol, timestamp, open_price, high_price, low_price, close_price, volume)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (symbol, datetime.fromtimestamp(timestamp / 1000), open_price, high_price, low_price, close_price, volume))

            conn.commit()

    

    





    
    

        




