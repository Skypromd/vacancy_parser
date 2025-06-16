import unittest
from unittest.mock import patch
from src.user_interaction import user_interaction


class TestUserInteraction(unittest.TestCase):
    @patch("builtins.input", side_effect=["5"])
    def test_exit(self, mock_input):
        with patch("builtins.print") as mock_print:
            user_interaction()
            mock_print.assert_any_call("Выход из программы.")
            mock_input.assert_called()

    @patch("src.api.hh_api.HeadHunterAPI.get_vacancies")
    @patch("builtins.input", side_effect=["1", "Python", "5"])
    def test_search_vacancies(self, mock_input, mock_get_vacancies):
        mock_get_vacancies.return_value = [
            {
                "name": "Test",
                "alternate_url": "https://hh.ru/vacancy/1",
                "salary": None,
                "snippet": {"requirement": "Test"},
            }
        ]
        with patch("builtins.print") as mock_print:
            user_interaction()
            mock_print.assert_any_call("Найдено 1 вакансий. Сохранено в файл.")
            mock_input.assert_called()

    @patch("src.storage.json_storage.JSONStorage.get_vacancies")
    @patch("builtins.input", side_effect=["2", "2", "5"])
    def test_top_n_vacancies(self, mock_input, mock_get_vacancies):
        mock_get_vacancies.return_value = [
            {
                "name": "V1",
                "alternate_url": "https://hh.ru/vacancy/1",
                "salary": "100000-100000 RUR",
                "snippet": {"requirement": "Test"},
            },
            {
                "name": "V2",
                "alternate_url": "https://hh.ru/vacancy/2",
                "salary": "200000-200000 RUR",
                "snippet": {"requirement": "Test"},
            },
        ]
        with patch("builtins.print") as mock_print:
            user_interaction()
            mock_print.assert_any_call("1. V2")
            mock_input.assert_called()

    @patch("src.storage.json_storage.JSONStorage.get_vacancies")
    @patch("builtins.input", side_effect=["3", "Test", "5"])
    def test_filter_vacancies(self, mock_input, mock_get_vacancies):
        mock_get_vacancies.return_value = [
            {
                "name": "V1",
                "alternate_url": "https://hh.ru/vacancy/1",
                "salary": "100000 RUR",
                "snippet": {"requirement": "Test description"},
            }
        ]
        with patch("builtins.print") as mock_print:
            user_interaction()
            mock_print.assert_any_call("1. V1")
            mock_input.assert_called()

    @patch("src.storage.json_storage.JSONStorage.get_vacancies")
    @patch("builtins.input", side_effect=["4", "100000-200000", "5"])
    def test_filter_by_salary(self, mock_input, mock_get_vacancies):
        mock_get_vacancies.return_value = [
            {
                "name": "V1",
                "alternate_url": "https://hh.ru/vacancy/1",
                "salary": "150000-150000 RUR",
                "snippet": {"requirement": "Test"},
            }
        ]
        with patch("builtins.print") as mock_print:
            user_interaction()
            mock_print.assert_any_call("1. V1")
            mock_input.assert_called()

    @patch("src.storage.json_storage.JSONStorage.get_vacancies")
    @patch("builtins.input", side_effect=["4", "100000", "5"])
    def test_filter_by_salary_single(self, mock_input, mock_get_vacancies):
        mock_get_vacancies.return_value = [
            {
                "name": "V1",
                "alternate_url": "https://hh.ru/vacancy/1",
                "salary": "150000-150000 RUR",
                "snippet": {"requirement": "Test"},
            }
        ]
        with patch("builtins.print") as mock_print:
            user_interaction()
            mock_print.assert_any_call("1. V1")
            mock_input.assert_called()

    @patch(
        "builtins.input",
        side_effect=[UnicodeDecodeError("utf-8", b"\xd0", 0, 1, "invalid"), "5"],
    )
    def test_unicode_decode_error(self, mock_input):
        with patch("builtins.print") as mock_print:
            user_interaction()
            mock_print.assert_any_call(
                "Ошибка ввода: используйте символы UTF-8 " "(например, латиницу)."
            )
            mock_print.assert_any_call("Выход из программы.")
            mock_input.assert_called()


if __name__ == "__main__":
    unittest.main()
