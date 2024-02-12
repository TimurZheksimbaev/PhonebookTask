from typing import Dict
from src.Phonebook import Phonebook
from src.PersonInfo import PersonInfo
from src.JsonManager import JsonManager
import sys
FILE_PATH = "phonebook.json" # замените на свой путь до json файла
import unittest


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.jm = JsonManager(FILE_PATH)
    def test_create(self):
        data = {
            "name": "amir",
            "surname": "bikeneev",
            "fathername": "al;sgdh",
            "organization": "aliexpress",
            "work_phone_number": "96798",
            "personal_phone_number": "25432356"

        }
        self.jm.write(data)
        json_data = self.jm.read()
        self.assertEqual(json_data[len(json_data)-1], data)

    def test_display(self):
        data = self.jm.read()
        self.assertNotEquals(data, None)

    def test_delete(self):
        data = {
            "name": "amir",
            "surname": "bikeneev",
            "fathername": "al;sgdh",
            "organization": "aliexpress",
            "work_phone_number": "96798",
            "personal_phone_number": "25432356"
        }
        self.jm.write(data)
        self.jm.delete(data)
        found = self.jm.search_exact(data)
        self.assertEqual(found, False)

if __name__ == "__main__":
    FILE_PATH = sys.argv[1]

    unittest.main()