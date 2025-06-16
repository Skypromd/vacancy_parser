import unittest
from src.models.vacancy import Vacancy
from src.utils.helpers import sort_vacancies, get_top_vacancies, \
                             filter_vacancies, print_vacancies


class TestHelpers(unittest.TestCase):

    def setUp(self):
        self.v1 = Vacancy("V1", "url1", {"from": 100000, "to": 100000},
                          "desc")
        self.v2 = Vacancy("V2", "url2", {"from": 200000, "to": 200000},
                          "desc")
        self.v3 = Vacancy("V3", "url3", None, "desc")

    def test_sort_vacancies(self):
        """Тестирует сортировку вакансий по зарплате."""
        vacancies = [self.v3, self.v2, self.v1]
        sorted_vacancies = sort_vacancies(vacancies)
        self.assertEqual(sorted_vacancies, [self.v1, self.v2, self.v3])

    def test_get_top_vacancies(self):
        """Тестирует получение топ-N вакансий."""
        vacancies = [self.v1, self.v2]
        top = get_top_vacancies(vacancies, 1)
        self.assertEqual(len(top), 1)
        self.assertEqual(top[0], self.v2)

    def test_filter_vacancies(self):
        """Тестирует фильтрацию вакансий по ключевым словам."""
        vacancies = [self.v1, self.v2]
        filtered = filter_vacancies(vacancies, ["V1"])
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0], self.v1)

    def test_print_vacancies_empty(self):
        """Тестирует вывод пустого списка вакансий."""
        with self.assertRaises(SystemExit):
            print_vacancies([])


if __name__ == "__main__":
    unittest.main()