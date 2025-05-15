import unittest
from src.models.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def test_valid_vacancy(self):
        vacancy = Vacancy(
            name="Python Developer",
            url="https://hh.ru/vacancy/123",
            salary={"from": 100000, "to": 150000, "currency": "RUR"},
            description="Требуется опыт"
        )
        self.assertEqual(vacancy.name, "Python Developer")
        self.assertEqual(vacancy.salary, "100000-150000 RUR")

    def test_invalid_salary(self):
        vacancy = Vacancy(
            name="Developer",
            url="https://hh.ru/vacancy/456",
            salary=None,
            description="Без опыта"
        )
        self.assertEqual(vacancy.salary, "Зарплата не указана")

    def test_salary_comparison(self):
        v1 = Vacancy("V1", "url", {"from": 100000, "to": 100000}, "desc")
        v2 = Vacancy("V2", "url", {"from": 200000, "to": 200000}, "desc")
        self.assertTrue(v1 < v2)


if __name__ == '__main__':
    unittest.main()
