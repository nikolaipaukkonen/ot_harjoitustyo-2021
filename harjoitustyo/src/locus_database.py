import sqlite3
from locus import Locus



def check_db(db_name):
    db = sqlite3.connect(str(db_name))
    db.isolation_level = None
    c = db.cursor()

    c.execute("PRAGMA foreign_keys = ON")

    # Initialize database
    try:
        c.execute("CREATE TABLE Locus \
                (id INTEGER PRIMARY KEY, \
                name TEXT UNIQUE, \
                descr TEXT, \
                thickness INTEGER, \
                above TEXT, \
                below TEXT)")
        c.execute(
            "CREATE TABLE Finds \
                (id INTEGER PRIMARY KEY, \
                find_type TEXT UNIQUE, \
                locus INTEGER REFERENCES Locus)")
        c.execute(
            "CREATE TABLE Samples \
            (id INTEGER PRIMARY KEY, \
            sample_type TEXT UNIQUE, \
            locus INTEGER REFERENCES Locus)")

        print(f"Database {db_name} created")

    except:
        print(f"Database {db_name} exists. Opening...")


def create_locus(name, descr, thick, above, below, db_name):
    db = sqlite3.connect(str(db_name))
    db.isolation_level = None
    c = db.cursor()

    try:
        c.execute("INSERT INTO Locus (\
        name, descr, thickness, above, below) \
        VALUES(?,?,?,?,?)")

    except:
        print("Virheellinen syöte")
