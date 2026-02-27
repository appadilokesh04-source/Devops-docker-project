import logging
import mysql.connector
import os
import time

class Database:
    def __init__(self):
        self.connect()

    def connect(self):
        while True:
            try:
                self.conn = mysql.connector.connect(
                    host=os.getenv("DB_HOST"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD"),
                    database=os.getenv("DB_NAME")
                )
                logging.info("Connected to MySQL successfully!")
                break
            except Exception as e:
                logging.warning("Waiting for MySQL...")
                time.sleep(3)
