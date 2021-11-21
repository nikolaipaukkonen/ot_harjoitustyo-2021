import unittest
import os
from pathlib import Path
from locus_database import check_db, create_locus

class TestLocus_database(unittest.TestCase):
    def setUp(self):
        self.db_name = "testi.db"

    def test_check_db_creates_new_files(self):
        check_db(self.db_name)
        path = Path(f'./{self.db_name}')
        assert path.is_file()
        os.remove(path)

    def test_create_locus(self):
        check_db(self.db_name)
        create_locus("surface", "packed turf", 15, "-", "-", self.db_name)
        #wip (implement read database)

    def test_read_db_name(self):
        f = open("db_list", "w+")
        check_db(self.db_name)
        db_name_from_file = f.readline()
        self.assertEqual(self.db_name, db_name_from_file)
        os.remove("db_list")
