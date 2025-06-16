from abc import ABC, abstractmethod


class AbstractFileStorage(ABC):
    """Абстрактный класс для работы с файлами."""

    @abstractmethod
    def get_data(self):
        """Получает данные из файла."""
        pass

    @abstractmethod
    def add_data(self, data):
        """Добавляет данные в файл."""
        pass

    @abstractmethod
    def delete_data(self, key):
        """Удаляет данные из файла по ключу."""
        pass