from abc import ABC, abstractmethod
from typing import List, Dict


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API платформ с вакансиями."""

    @abstractmethod
    def connect(self) -> None:
        """Подключение к API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str) -> List[Dict]:
        """Получение вакансий по ключевому слову."""
        pass
