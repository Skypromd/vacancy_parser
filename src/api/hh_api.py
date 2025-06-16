# src/api/hh_api.py
from src.api.abstract_api import AbstractAPI
import requests

class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"
        self.headers = {
            "User-Agent": "houston42@gmail.com"
        }

    def connect(self):
        """Устанавливает соединение с API HH.ru."""
        pass  # Можно добавить реальную логику, если нужно

    def get_vacancies(self, search_query: str) -> list[dict]:
        """Получает список вакансий по ключевому слову с API HH.ru."""
        params = {"text": search_query, "per_page": 100}
        response = requests.get(self.base_url, params=params, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        print(f"Данные от API: {data}")  # Отладочный вывод
        return data.get("items", [])
