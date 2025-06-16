from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def connect(self):
        """Устанавливает соединение с API."""
        pass

    @abstractmethod
    def get_vacancies(self, search_query):
        """Получает список вакансий по ключевому слову."""
        pass