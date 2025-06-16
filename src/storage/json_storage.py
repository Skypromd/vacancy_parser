from src.storage.abstract_file_storage import AbstractFileStorage
import json
import os
from typing import Dict


class JSONStorage(AbstractFileStorage):
    """Класс для работы с хранилищем вакансий в формате JSON."""

    def __init__(self, file_path: str = "vacancies.json"):
        """Инициализация хранилища с возможностью указания пути к файлу."""
        self._file_path = file_path
        self._load_data()

    def _load_data(self):
        """Загрузка данных из файла."""
        if os.path.exists(self._file_path):
            try:
                with open(self._file_path, 'r', encoding='utf-8') as file:
                    self.data = json.load(file)
            except json.JSONDecodeError:
                self.data = []
        else:
            self.data = []

    def get_data(self):
        """Получает данные из файла."""
        self._load_data()
        return self.data

    def add_data(self, data: Dict):
        """Добавляет данные в файл, избегая дублей по URL."""
        print(f"Добавление вакансии в JSON: данные={data}, "
              f"url={data.get('alternate_url')}, "
              f"type(url)={type(data.get('alternate_url'))}")
        self._load_data()
        if not any(v.get('alternate_url') == data.get('alternate_url')
                   for v in self.data):
            self.data.append(data)
        with open(self._file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def delete_data(self, key: str):
        """Удаляет данные из файла по ключу."""
        self._load_data()
        self.data = [v for v in self.data if v.get('id') != key]
        with open(self._file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)