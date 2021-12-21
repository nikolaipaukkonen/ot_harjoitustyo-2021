''' Tietokantojen luominen ja täydentäminen, kutsutaan mainView.py:stä käsin '''

import sqlite3
import csv

def check_db(db_name):
    ''' Tarkistaa onko tietokantaa olemassa ja luo sellaisen, jos ei ole .

    Args:
        db_name: Käytettävän tietokannan nimi.

    '''

    current_db = sqlite3.connect(str(db_name))
    file=open("db_list", "w+", encoding="utf-8")
    file.write(f"{db_name}")
    current_db.isolation_level = None
    cursor = current_db.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

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
            sample_type TEXT, \
            locus INTEGER REFERENCES Locus)")

        print(f"Database {db_name} created")

    except Exception:
        print(f"Database {db_name} exists. Opening...")

def read_db_name():
    ''' Lukee tietokannan nimen "muistista".

    Returns:
        Tietokannan nimi merkkijonona.
    '''

    file = open("db_list", "r", encoding="utf-8")
    db_name = file.readline()
    return db_name

def create_locus(locus):
    ''' Funktio luo stratigrafisen yksikön (olion) ja vie sen tietokantaan

    Args:
        locus: Stratigrafinen yksikkö, joka syötetään tietokantaan.
    '''

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
    ''' Hae ja tulosta näkymään stratigrafiset yksiköt (locukset)

    Returns:
        Locus-taulukon sisältö riveinä.
    '''

    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    cursor.execute("SELECT * FROM Locus")

    rows = (cursor.fetchall())
    return rows

def fetch_locus_ids():
    ''' Hakee ja palauttaa näkymään stratigrafiten yksiköiden id-numerot.

    Returns:
        Lista locusten id-numeroista.
    '''

    rows = fetch_loci()
    locus_ids = []

    for row in rows:
        locus_ids.append(row[0])

    return locus_ids

def fetch_finds():
    ''' Hakee ja palauttaa löydöt tietokannasta.

    Returns:
        Löytöjen tiedot riveittäin.
    '''

    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    cursor.execute("SELECT * FROM Finds")
    rows = (cursor.fetchall())
    return rows

def fetch_samples():
    '''Hakee ja palauttaa näytteet tietokannata.

    Returns:
        Näytteiden tiedot riveinä.
    '''

    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()

    cursor.execute("SELECT * FROM Samples")
    rows = (cursor.fetchall())
    return rows

def create_find(find):
    ''' Funktio luo löytö-olion ja vie sen tietokantaan.

    Args:
        find: Löytö-olio, joka viedään tietokantaan.
    '''

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
    '''Funktio luo näyte-olion ja vie sen tietokantaan.

    Args:
        sample: Näyte-olio, joka viedään tietokantaan.
    '''

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

        print(f"Sample of type {sample.sample_type} added to database")

    except:
        print("Input error in create_sample")

def remove_locus(id_no):
    ''' Poistaa locuksen tietokannasta id:n perusteella.

    Args:
        id_no: id-numero (kokonaisluku), jonka perusteella poisto tehdään.
    '''

    db_name = read_db_name()

    current_database = sqlite3.connect(str(db_name))
    current_database.isolation_level = None
    cursor = current_database.cursor()
    
    try:
        cursor.execute(f"DELETE FROM Locus WHERE id={id_no}")
    except:
        print("Error in remove locus")

def export_data(filename):
    ''' Vie tietokannan kolmeksi erilliseksi csv-tiedostoksi (yksiköt, löydöt ja näytteet).

    Args:
        filename: merkkijono, joka tulee luotavien tiedostojen alkuun.
    '''

    with open(f"{filename}_stratigraphy.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Id","Type", "Name", "Description", "Thickness", "Above"])
        rows = fetch_loci()
        writer.writerows(rows)
        print("Export locus data performed")

    with open(f"{filename}_finds.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Id","Find type", "Dating", "Description", "Weight", "Locus"])
        rows = fetch_finds()
        writer.writerows(rows)
        print("Export find data performed")

    with open(f"{filename}_samples.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Id","Sample type", "Locus"])
        rows = fetch_samples()
        writer.writerows(rows)
        print("Export sample data performed")
