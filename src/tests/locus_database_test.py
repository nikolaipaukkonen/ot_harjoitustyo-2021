''' Testit locus_databaselle '''

import unittest
import os
from pathlib import Path
from database.locus_database import export_data,check_db,create_find,create_locus,create_sample,remove_locus,fetch_finds,fetch_loci,fetch_locus_ids,fetch_samples
from database.locus import Locus
from database.find import Find
from database.sample import Sample


class TestLocus_database(unittest.TestCase):
    ''' Luo testitietokannan ja testaa sitä vasten eri funktioita'''
    
    def setUp(self):
        ''' Kirjoittaa uuden testitietokannan '''
        self.db_name = "testi.db"

    def test_check_db_creates_new_files(self):
        ''' Testataan, syntyykö tietokanta'''
        check_db(self.db_name)
        path = Path(f'./{self.db_name}')
        assert path.is_file()
        os.remove(path)

    def test_create_find(self):
        ''' Luodaan löytö ja tarkistetaan, löytyykö se tietokannasta'''
        check_db(self.db_name)
        find = Find("Gold", "Iron age", "Gold coin", 21, 0)
        create_find(find)

        rows = fetch_finds()
        self.assertEqual(rows[0][1], "Gold")

    def test_create_100_finds(self):
        ''' Luodaan 100 löytöä ja tarkistetaan tietokannan rivien pituus'''
        check_db(self.db_name)
        for _ in range(100):
            find = Find("Gold", "Iron age", "Gold coin", 21, 0)
            create_find(find)

        rows = fetch_finds()
        self.assertEqual(len(rows), 100)

    def test_create_locus(self):
        ''' Luodaan yksikkö ja tarkistetaan, löytyykö se tietokannasta'''
        check_db(self.db_name)
        locus = Locus("Soil", "Top soil", "Loose gravel", 10, 0)
        create_locus(locus)

        rows = fetch_loci()
        self.assertEqual(rows[0][1], "Soil")

    def test_create_100_loci(self):
        ''' Luodaan 100 yksiköä ja tarkistetaan luotujen tietueiden määrä tietokannasta'''
        check_db(self.db_name)
        for i in range(100):
            name = str(i) + " layer"
            locus = Locus("Soil", name, "Loose gravel", 10, 0)
            create_locus(locus)

        rows = fetch_loci()
        self.assertEqual(len(rows), 100)

    def test_create_sample(self):
        ''' Luodaan näyte ja testataan löytyykö se tietokannasta'''
        check_db(self.db_name)
        sample = Sample("Soil", 1)
        create_sample(sample)

        rows = fetch_samples()
        self.assertEqual(rows[0][1], "Soil")

    def test_create_100_samples(self):
        ''' Luodaan 100 näytettä ja testataan Samplesin koko'''
        check_db(self.db_name)
        for _ in range(100):
            sample = Sample("Soil", 1)
            create_sample(sample)

        rows = fetch_samples()
        self.assertEqual(len(rows), 100)

    def test_read_db_name(self):
        ''' Luetaan väliaikaisesta db_lististä tietokannan nimi ja verrataan sitä '''
        file = open("db_list", "w+", encoding="utf-8")
        check_db(self.db_name)
        db_name_from_file = file.readline()
        self.assertEqual(self.db_name, db_name_from_file)
        os.remove("db_list")

    def test_fetch_locus_ids_returns_id(self):
        ''' Luodaan testilocus ja testataan locusten id:n hakua '''
        check_db(self.db_name)
        locus = Locus("Soil", "Top soil", "Loose gravel", 10, 0)
        create_locus(locus)
        test_ids = fetch_locus_ids()
        self.assertEqual(1, test_ids[0])

    def test_remove_locus(self):
        check_db(self.db_name)

        remove_locus(1)

        rows = fetch_loci()
        self.assertEqual(100, len(rows))

    def test_export_data_creates_stratigraphy_file(self):
        ''' Kutsutaan export_dataa ja tarkistetaan, että syntyy kolme csv:tä'''
        check_db(self.db_name)
        export_data(self.db_name)
        path_strat = Path(f'./{self.db_name}_stratigraphy.csv')
        path_finds = Path(f'./{self.db_name}_finds.csv')
        path_samples = Path(f'./{self.db_name}_samples.csv')
        assert path_strat.is_file()
        os.remove(path_strat)
        os.remove(path_finds)
        os.remove(path_samples)
