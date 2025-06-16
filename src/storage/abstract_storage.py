from abc import ABC, abstractmethod
from typing import List, Dict


class AbstractStorage(ABC):
    """Абстрактный класс для работы с хранилищем вакансий."""

    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        """Добавление вакансии в хранилище."""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict) -> List[Dict]:
        """Получение вакансий по критериям."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Dict) -> None:
        """Удаление вакансии из хранилища."""
        pass
