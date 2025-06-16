from src.api.abstract_api import AbstractAPI
import requests


class HeadHunterAPI(AbstractAPI):
    """Класс для взаимодействия с API HH.ru."""

    def __init__(self):
        self._base_url = "https://api.hh.ru/vacancies"
        self._headers = {
            "User-Agent": "houston42@gmail.com"
        }

    def _connect(self):
        """Устанавливает соединение с API HH.ru с проверкой статуса."""
        response = requests.get(self._base_url, headers=self._headers)
        response.raise_for_status()

    def get_vacancies(self, search_query: str) -> list[dict]:
        """Получает список вакансий по ключевому слову с API HH.ru."""
        self._connect()
        params = {"text": search_query, "per_page": 100}
        response = requests.get(self._base_url, params=params, headers=self._headers)
        response.raise_for_status()
        data = response.json()
        print(f"Данные от API: {data}")  # Отладочный вывод
        return data.get("items", [])
