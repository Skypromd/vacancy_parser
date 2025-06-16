import unittest
from src.api.hh_api import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):
    def setUp(self):
        self.api = HeadHunterAPI()

    def test_get_vacancies(self):
        vacancies = self.api.get_vacancies("Python")
        self.assertIsInstance(vacancies, list)
        if vacancies:
            self.assertIsInstance(vacancies[0], dict)


if __name__ == "__main__":
    unittest.main()
