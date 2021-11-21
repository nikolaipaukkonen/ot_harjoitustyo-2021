title Päätoiminnallisuudet

projekti->gui : click "Create / add database"
gui->locus_database : check_db("tietokanta.db")
locus_database->sqlite : CREATE TABLE(...)

gui->locus_database : add_locus (tyyppi, nimi ...)
locus_database->sqlite : INSERT INTO Locus (...)

gui->locus_database : add_find (tyyppi, kuvaus, ...)
locus_database->sqlite : INSERT INTO Finds (...)
