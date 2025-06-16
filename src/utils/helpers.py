from typing import List
from src.models.vacancy import Vacancy


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка вакансий по зарплате."""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """Получение топ-N вакансий."""
    return vacancies[:n]


def filter_vacancies(vacancies: List[Vacancy], keywords: List[str]) -> List[Vacancy]:
    """Фильтрация вакансий по ключевым словам."""
    if not keywords:
        return vacancies
    return [
        v
        for v in vacancies
        if any(keyword.lower() in v._description.lower() for keyword in keywords)
    ]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Вывод вакансий в консоль."""
    if not vacancies:
        print("Вакансии не найдены.")
        return
    for i, vacancy in enumerate(vacancies, 1):
        print(f"{i}. {vacancy.name}")
        print(f"Зарплата: {vacancy.salary}")
        print(f"Ссылка: {vacancy._url}")
        print(f"Описание: {vacancy._description}")
        print("-" * 50)
