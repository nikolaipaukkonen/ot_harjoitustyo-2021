''' Tietokantojen luominen ja täydentäminen, käytetään mainView.py:stä käsin '''

import sqlite3
import csv
from database.locus import Locus
from database.find import Find

def check_db(db_name):
    ''' Tarkista onko tietokantaa olemassa ja luo sellainen jos ei ole '''

    db = sqlite3.connect(str(db_name))
    f=open("db_list", "w+")
    f.write(f"{db_name}")
    db.isolation_level = None
    c = db.cursor()

    c.execute("PRAGMA foreign_keys = ON")

    # Initialize database
    try:
        c.execute("CREATE TABLE Locus \
                (id INTEGER PRIMARY KEY, \
                type TEXT, \
                name TEXT UNIQUE, \
                descr TEXT, \
                thickness INTEGER, \
                above INTEGER REFERENCES Locus)")
        c.execute(
            "CREATE TABLE Finds \
                (id INTEGER PRIMARY KEY, \
                find_type TEXT, \
                dating TEXT, \
                descr, TEXT, \
                weight INTEGER, \
                locus INTEGER REFERENCES Locus)")
        c.execute(
            "CREATE TABLE Samples \
            (id INTEGER PRIMARY KEY, \
            sample_type TEXT UNIQUE, \
            locus INTEGER REFERENCES Locus)")

        print(f"Database {db_name} created")

    except:
        print(f"Database {db_name} exists. Opening...")

def read_db_name():
    ''' Lue tietokannan nimi "muistista" '''
    f = open("db_list", "r")
    db_name = f.readline()
    return db_name

def create_locus(locus):
    ''' Funktio luo stratigrafisen yksikön (olion) ja vie sen tietokantaan '''

    db_name = read_db_name()

    db = sqlite3.connect(str(db_name))
    db.isolation_level = None
    c = db.cursor()

    try:
        c.execute("INSERT INTO Locus (type, name, descr, thickness, above) \
            VALUES(?,?,?,?,?)", (
                locus.l_type,
                locus.name,
                locus.descr,
                locus.thick,
                locus.above)
                )

        print(f"Locus {locus.name} added to database")

    except:
        print("Input error in create_locus")

def fetch_loci():
    ''' Hae ja tulosta näkymään stratigrafiset yksiköt (locukset) '''
    db_name = read_db_name()

    db = sqlite3.connect(str(db_name))
    db.isolation_level = None
    c = db.cursor()

    c.execute("SELECT * FROM Locus")

    rows = (c.fetchall())
    return rows

def fetch_locus_ids():
    rows = fetch_loci()
    locus_ids = []

    for row in rows:
        locus_ids.append(row[0])

    return locus_ids

def fetch_finds():
    ''' Hae ja tulosta näkymään löydöt '''
    db_name = read_db_name()

    db = sqlite3.connect(str(db_name))
    db.isolation_level = None
    c = db.cursor()

    c.execute("SELECT * FROM Finds")
    rows = (c.fetchall())
    return rows

def create_find(find):
    ''' Funktio luo löytö-olion ja vie sen tietokantaan'''

    db_name = read_db_name()

    db = sqlite3.connect(str(db_name))
    db.isolation_level = None
    c = db.cursor()

    print("Creating find", find.find_type)
    try:
        c.execute("INSERT INTO Finds (find_type, dating, descr, weight, locus) \
            VALUES(?,?,?,?,?)", (
                find.find_type,
                find.dating,
                find.descr,
                find.weight,
                find.locus))

        print(f"Find {find.find_type} added to database")

    except:
        print("Input error in create_find")

def export_data(filename):
    with open(f"{filename}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Type", "Name", "Description", "Thickness", "Above"])
        rows = fetch_loci()
        writer.writerows(rows)
        print("Export data performed")
        