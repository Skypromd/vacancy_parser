import json
import os
from typing import Dict


class JSONStorage:
    """Класс для работы с хранилищем вакансий в формате JSON."""

    def __init__(self, file_path: str = "vacancies.json"):
        """Инициализация хранилища с возможностью указания пути к файлу."""
        self.file_path = file_path
        self._load_data()

    def _load_data(self):
        """Загрузка данных из файла."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as file:
                    self.data = json.load(file)
            except json.JSONDecodeError:
                self.data = []
        else:
            self.data = []

    def add_vacancy(self, vacancy: Dict):
        """Добавление вакансии в хранилище."""
        print(
            f"Добавление вакансии в JSON: данные={vacancy}, url={vacancy.get('alternate_url')}, "
            f"type(url)={type(vacancy.get('alternate_url'))}"
        )
        self._load_data()
        self.data.append(vacancy)
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def get_vacancies(self, criteria: Dict) -> list:
        """Получение вакансий по критериям."""
        self._load_data()
        if not criteria:
            return self.data
        keyword = criteria.get("keyword", "").lower()
        return [
            v
            for v in self.data
            if keyword in v.get("name", "").lower()
            or keyword in v.get("snippet", {}).get("requirement", "").lower()
        ]

    def delete_vacancy(self, vacancy_id: str):
        """Удаление вакансии по идентификатору."""
        self._load_data()
        self.data = [v for v in self.data if v.get("id") != vacancy_id]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
