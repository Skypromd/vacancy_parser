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

    def test_invalid_name(self):
        vacancy = Vacancy("", "url", None, "desc")
        self.assertEqual(vacancy.name, "Название не указано")
        vacancy = Vacancy(None, "url", None, "desc")
        self.assertEqual(vacancy.name, "Название не указано")

    def test_invalid_url(self):
        vacancy = Vacancy("Test", "", None, "desc")
        self.assertEqual(vacancy._url, "URL не указан")
        vacancy = Vacancy("Test", None, None, "desc")
        self.assertEqual(vacancy._url, "URL не указан")

    def test_salary_only_from(self):
        vacancy = Vacancy(
            name="Test",
            url="url",
            salary={"from": 100000, "to": None, "currency": "RUR"},
            description="desc"
        )
        self.assertEqual(vacancy.salary, "от 100000 RUR")

    def test_salary_only_to(self):
        vacancy = Vacancy(
            name="Test",
            url="url",
            salary={"from": None, "to": 150000, "currency": "RUR"},
            description="desc"
        )
        self.assertEqual(vacancy.salary, "до 150000 RUR")

    def test_invalid_description_empty(self):
        vacancy = Vacancy("Test", "url", None, "")
        self.assertEqual(vacancy._description, "Описание не указано")

    def test_invalid_description_none(self):
        vacancy = Vacancy("Test", "url", None, None)
        self.assertEqual(vacancy._description, "Описание не указано")

    def test_invalid_comparison(self):
        v1 = Vacancy("V1", "url", {"from": 100000, "to": 100000}, "desc")
        with self.assertRaises(TypeError):
            v1 < "not a vacancy"

    def test_parse_salary_error(self):
        vacancy = Vacancy("Test", "url", None, "desc")
        vacancy._salary = "invalid"
        self.assertEqual(vacancy.parse_salary(), 0)

    def test_to_dict(self):
        vacancy = Vacancy("Test", "url", {"from": 100000, "to": 100000}, "desc")
        result = vacancy.to_dict()
        self.assertEqual(result, {
            'name': "Test",
            'alternate_url': "url",
            'salary': "100000-100000 RUR",
            'snippet': {'requirement': "desc"}
        })

    def test_cast_to_object_list_invalid(self):
        vacancies = [
            {
                'name': '',
                'alternate_url': '',
                'salary': None,
                'snippet': {'requirement': 'Test'}
            },
            {
                'name': 'Test',
                'alternate_url': 'url',
                'salary': None,
                'snippet': {'requirement': 'Test'}
            }
        ]
        result = Vacancy.cast_to_object_list(vacancies)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, "Название не указано")
        self.assertEqual(result[0]._url, "URL не указан")
        self.assertEqual(result[1].name, "Test")


if __name__ == "__main__":
    unittest.main()
