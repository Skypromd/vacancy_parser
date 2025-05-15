import requests
from typing import List, Dict
from .abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {
            'User-Agent': 'VacancyParser/1.0 (your_real_email@example.com)',  # Убедитесь, что email актуален
            'Accept': 'application/json'
        }
        self._params = {'text': '', 'page': 0, 'per_page': 100, 'area': '113'}  # Россия
        self._vacancies = []

    def connect(self) -> None:
        """Проверка подключения к API."""
        try:
            response = requests.get('https://api.hh.ru/areas', headers=self._headers, timeout=5)
            if response.status_code != 200:
                raise ConnectionError(f"Ошибка подключения: {response.status_code}")
        except requests.RequestException as e:
            raise ConnectionError(f"Ошибка подключения к API: {str(e)}")

    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получение вакансий с hh.ru по ключевому слову."""
        if not keyword or not isinstance(keyword, str):
            raise ValueError("Ключевое слово должно быть непустой строкой")

        self.connect()
        self._params['text'] = keyword.strip()
        self._params['page'] = 0
        self._vacancies = []

        try:
            while self._params['page'] < 20:
                response = requests.get(self._url, headers=self._headers, params=self._params, timeout=5)
                if response.status_code != 200:
                    raise ValueError(f"Ошибка запроса: {response.status_code}")
                data = response.json()
                self._vacancies.extend(data.get('items', []))
                self._params['page'] += 1
                if self._params['page'] >= data.get('pages', 0):
                    break
        except requests.RequestException as e:
            raise ValueError(f"Ошибка при получении вакансий: {str(e)}")

        return self._vacancies
