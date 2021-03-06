import os
import unittest
from database import Database


class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = ''
        cls.password = ''
        cls.filename = 'trader.db'
        cls.db = Database(database_filename=cls.filename)

    @classmethod
    def tearDownClass(cls):
        cls.db.close()
        os.remove(cls.filename)

    def test_00_initialize(self):
        self.db.initialize()

    def test_01_insert_user(self):
        self.db.insert_user(login=self.login, password=self.password)

    def test_02_valid_user(self):
        self.db.is_valid_user(login=self.login, password=self.password)


if __name__ == '__main__':
    unittest.main()
