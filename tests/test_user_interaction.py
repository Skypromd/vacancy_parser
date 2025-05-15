import unittest
from unittest.mock import patch
from src.user_interaction import user_interaction

class TestUserInteraction(unittest.TestCase):
    @patch('builtins.input', side_effect=['4'])
    def test_exit(self, mock_input):
        with patch('builtins.print') as mock_print:
            user_interaction()
            mock_print.assert_any_call("Выход из программы.")

    @patch('src.api.hh_api.HeadHunterAPI.get_vacancies')
    @patch('builtins.input', side_effect=['1', 'Python', '4'])
    def test_search_vacancies(self, mock_input, mock_get_vacancies):
        mock_get_vacancies.return_value = [
            {'name': 'Test', 'alternate_url': 'https://hh.ru/vacancy/1', 'salary': None, 'snippet': {'requirement': 'Test'}}
        ]
        with patch('builtins.print') as mock_print:
            user_interaction()
            mock_print.assert_any_call("Найдено 1 вакансий. Сохранено в файл.")

    @patch('src.storage.json_storage.JSONStorage.get_vacancies')
    @patch('builtins.input', side_effect=['2', '2', '4'])
    def test_top_n_vacancies(self, mock_input, mock_get_vacancies):
        mock_get_vacancies.return_value = [
            {'name': 'V1', 'alternate_url': 'https://hh.ru/vacancy/1', 'salary': {'from': 100000, 'to': 100000, 'currency': 'RUR'}, 'snippet': {'requirement': 'Test'}},
            {'name': 'V2', 'alternate_url': 'https://hh.ru/vacancy/2', 'salary': {'from': 200000, 'to': 200000, 'currency': 'RUR'}, 'snippet': {'requirement': 'Test'}}
        ]
        with patch('builtins.print') as mock_print:
            user_interaction()
            mock_print.assert_any_call("1. V2")

    @patch('src.storage.json_storage.JSONStorage.get_vacancies')
    @patch('builtins.input', side_effect=['3', 'Test', '4'])
    def test_filter_vacancies(self, mock_input, mock_get_vacancies):
        mock_get_vacancies.return_value = [
            {'name': 'V1', 'alternate_url': 'https://hh.ru/vacancy/1', 'salary': {'from': 100000, 'to': 100000, 'currency': 'RUR'}, 'snippet': {'requirement': 'Test description'}}
        ]
        with patch('builtins.print') as mock_print:
            user_interaction()
            mock_print.assert_any_call("1. V1")

if __name__ == "__main__":
    unittest.main()
