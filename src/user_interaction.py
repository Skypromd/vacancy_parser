from typing import List
from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_storage import JSONStorage
from src.utils.helpers import sort_vacancies, get_top_vacancies, filter_vacancies, print_vacancies


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    hh_api = HeadHunterAPI()
    json_saver = JSONStorage()

    while True:
        print("\n1. Поиск вакансий")
        print("2. Показать топ-N вакансий по зарплате")
        print("3. Фильтровать вакансии по ключевому слову")
        print("4. Выход")
        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            search_query = input("Введите поисковый запрос: ")
            try:
                vacancies = hh_api.get_vacancies(search_query)
                vacancy_objects = Vacancy.cast_to_object_list(vacancies)
                for vacancy in vacancy_objects:
                    json_saver.add_vacancy(vacancy.to_dict())
                print(f"Найдено {len(vacancy_objects)} вакансий. Сохранено в файл.")
            except Exception as e:
                print(f"Ошибка при поиске: {str(e)}")

        elif choice == '2':
            try:
                top_n = int(input("Введите количество вакансий для вывода: "))
                vacancies = json_saver.get_vacancies({})
                vacancy_objects = Vacancy.cast_to_object_list(vacancies)
                sorted_vacancies = sort_vacancies(vacancy_objects)
                top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
                print_vacancies(top_vacancies)
            except ValueError:
                print("Введите корректное число.")

        elif choice == '3':
            filter_words = input("Введите ключевые слова через пробел: ").split()
            vacancies = json_saver.get_vacancies({'keyword': ' '.join(filter_words)})
            vacancy_objects = Vacancy.cast_to_object_list(vacancies)
            filtered_vacancies = filter_vacancies(vacancy_objects, filter_words)
            print_vacancies(filtered_vacancies)

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")
