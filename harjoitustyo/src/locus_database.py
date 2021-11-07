import sqlite3
import time

db_name = "placeholder"
db = sqlite3.connect(str(db_name), ".db")
db.isolation_level = None

c = db.cursor()