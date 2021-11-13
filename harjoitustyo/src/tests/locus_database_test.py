import unittest
import os
from locus_database import check_db
from pathlib import Path

class TestLocus_database(unittest.TestCase):
    def setUp(self):
        self.db_name = "testi.db"

    def test_check_db_creates_new_files(self):
        check_db(self.db_name)
        path = Path(f'./{self.db_name}')
        assert path.is_file()
        os.remove(path)