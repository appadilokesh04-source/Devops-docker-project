import logging
from flask import Flask
from db import Database


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
db = Database()

@app.route("/")
def home():
    logging.info("Home page accessed")
    return "Flask + MySQL + ENV variables working 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
