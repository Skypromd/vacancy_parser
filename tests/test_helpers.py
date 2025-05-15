import unittest
from unittest.mock import patch
from src.models.vacancy import Vacancy
from src.utils.helpers import sort_vacancies, get_top_vacancies, filter_vacancies, print_vacancies

class TestHelpers(unittest.TestCase):
    def setUp(self):
        self.vacancy1 = Vacancy(
            name="Developer",
            url="https://hh.ru/vacancy/1",
            salary={"from": 100000, "to": 100000, "currency": "RUR"},
            description="Python experience"
        )
        self.vacancy2 = Vacancy(
            name="Senior Developer",
            url="https://hh.ru/vacancy/2",
            salary={"from": 200000, "to": 200000, "currency": "RUR"},
            description="Java experience"
        )
        self.vacancies = [self.vacancy1, self.vacancy2]

    def test_sort_vacancies(self):
        sorted_vacs = sort_vacancies(self.vacancies)
        self.assertEqual(sorted_vacs[0].name, "Senior Developer")  # Самая высокая зарплата первая
        self.assertEqual(sorted_vacs[1].name, "Developer")

    def test_get_top_vacancies(self):
        top_vacs = get_top_vacancies(self.vacancies, 1)
        self.assertEqual(len(top_vacs), 1)
        self.assertEqual(top_vacs[0].name, "Developer")

    def test_filter_vacancies(self):
        filtered_vacs = filter_vacancies(self.vacancies, ["Python"])
        self.assertEqual(len(filtered_vacs), 1)
        self.assertEqual(filtered_vacs[0].name, "Developer")
        filtered_vacs = filter_vacancies(self.vacancies, ["C++"])
        self.assertEqual(len(filtered_vacs), 0)

    def test_print_vacancies_empty(self):
        with patch('builtins.print') as mock_print:
            print_vacancies([])
            mock_print.assert_called_with("Вакансии не найдены.")

if __name__ == "__main__":
    unittest.main()
