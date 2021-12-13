''' Tietokantojen luominen ja täydentäminen, käytetään mainView.py:stä käsin '''

import sqlite3
import csv
from database.locus import Locus
from database.find import Find
from database.sample import Sample

def check_db(db_name):
    ''' Tarkista onko tietokantaa olemassa ja luo sellainen jos ei ole '''

    current_db = sqlite3.connect(str(db_name))
    file=open("db_list", "w+", encoding="utf-8")
    file.write(f"{db_name}")
    current_db.isolation_level = None
    cursor = current_db.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    # Initialize database
    try:
        cursor.execute("CREATE TABLE Locus \
                (id INTEGER PRIMARY KEY, \
                type TEXT, \
                name TEXT UNIQUE, \
                descr TEXT, \
                thickness INTEGER, \
                above INTEGER REFERENCES Locus)")
        cursor.execute(
            "CREATE TABLE Finds \
                (id INTEGER PRIMARY KEY, \
                find_type TEXT, \
                dating TEXT, \
                descr, TEXT, \
                weight INTEGER, \
                locus INTEGER REFERENCES Locus)")
        cursor.execute(
            "CREATE TABLE Samples \
            (id INTEGER PRIMARY KEY, \
            sample_type TEXT UNIQUE, \
            locus INTEGER REFERENCES Locus)")

        print(f"Database {db_name} created")

    except:
        print(f"Database {db_name} exists. Opening...")

def read_db_name():
    ''' Lue tietokannan nimi "muistista" '''
    file = open("db_list", "r", encoding="utf-8")
    db_name = file.readline()
    return db_name

def create_locus(locus):
    ''' Funktio luo stratigrafisen yksikön (olion) ja vie sen tietokantaan '''

    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    try:
        cursor.execute("INSERT INTO Locus (type, name, descr, thickness, above) \
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

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    cursor.execute("SELECT * FROM Locus")

    rows = (cursor.fetchall())
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

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    cursor.execute("SELECT * FROM Finds")
    rows = (cursor.fetchall())
    return rows

def fetch_samples():
    '''Hae näytteet'''
    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    cursor.execute("SELECT * FROM Samples")
    rows = (cursor.fetchall())
    return rows

def create_find(find):
    ''' Funktio luo löytö-olion ja vie sen tietokantaan'''

    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    print("Creating find", find.find_type)
    try:
        cursor.execute("INSERT INTO Finds (find_type, dating, descr, weight, locus) \
            VALUES(?,?,?,?,?)", (
                find.find_type,
                find.dating,
                find.descr,
                find.weight,
                find.locus))

        print(f"Find {find.find_type} added to database")

    except:
        print("Input error in create_find")

def create_sample(sample):
    '''Funktio luo näyte-olion ja vie sen tietokantaan'''
    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    print("Creating sample", sample.sample_type)

    try:
        cursor.execute("INSERT INTO Samples (sample_type, locus) \
            VALUES(?,?)", (
                sample.sample_type,
                sample.sample_locus))

        print(f"Find {sample.sample_type} added to database")

    except:
        print("Input error in create_sample")

def remove_locus(id):
    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()
    print(f"Removing locus DEBUD, removing id {id}")
    try:
        cursor.execute(f"DELETE FROM Locus WHERE id={id}")
    except:
        print("Error in remove locus")

def export_data(filename):
    with open(f"{filename}_stratigraphy.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Id","Type", "Name", "Description", "Thickness", "Above"])
        rows = fetch_loci()
        writer.writerows(rows)
        print("Export locus data performed")
    
    with open(f"{filename}_finds.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Id","Find type", "Dating", "Description", "Weight", "Locus"])
        rows = fetch_finds()
        writer.writerows(rows)
        print("Export find data performed")

    with open(f"{filename}_samples.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Id","Sample type", "Locus"])
        rows = fetch_samples()
        writer.writerows(rows)
        print("Export sample data performed")
        