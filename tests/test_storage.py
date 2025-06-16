import unittest
import os
from src.storage.json_storage import JSONStorage


class TestJSONStorage(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_vacancies.json"
        self.storage = JSONStorage(self.test_file)
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_vacancy(self):
        vacancy = {
            "name": "Test Job",
            "alternate_url": "https://hh.ru/vacancy/1",
            "salary": "100000 RUR",
        }
        self.storage.add_vacancy(vacancy)
        self.assertEqual(len(self.storage.data), 1)
        self.assertEqual(self.storage.data[0], vacancy)

    def test_delete_vacancy(self):
        vacancy = {
            "id": "1",
            "name": "Test Job",
            "alternate_url": "https://hh.ru/vacancy/1",
            "salary": "100000 RUR",
        }
        self.storage.add_vacancy(vacancy)
        self.storage.delete_vacancy("1")
        self.assertEqual(len(self.storage.data), 0)

    def test_get_vacancies_with_criteria(self):
        vacancy1 = {
            "name": "Python Job",
            "alternate_url": "https://hh.ru/vacancy/2",
            "salary": "200000 RUR",
        }
        vacancy2 = {
            "name": "Java Job",
            "alternate_url": "https://hh.ru/vacancy/3",
            "salary": "150000 RUR",
        }
        self.storage.add_vacancy(vacancy1)
        self.storage.add_vacancy(vacancy2)
        result = self.storage.get_vacancies({"keyword": "python"})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], vacancy1)


if __name__ == "__main__":
    unittest.main()
