from typing import Optional
import re


class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ('_name', '_url', '_salary', '_description')

    def __init__(self, name: str, url: str, salary: Optional[dict | str], description: Optional[str]):
        print(f"Инициализация Vacancy: name={name}, url={url}, type(url)={type(url)}, "
              f"salary={salary}, type(salary)={type(salary)}, description={description}, "
              f"type(description)={type(description)}")
        if url is None or (isinstance(url, str) and not url.strip()):
            url = "URL не указан"
            print(f"Предупреждение: url заменён на 'URL не указан' из-за: {url}, type={type(url)}")
        self._name = self._validate_name(name)
        self._url = self._validate_url(url)
        self._salary = self._validate_salary(salary)
        self._description = self._validate_description(description)

    @staticmethod
    def _validate_name(name: Optional[str]) -> str:
        """Валидация названия вакансии."""
        print(f"Валидация name: {name}, type={type(name)}")
        if name is None or not isinstance(name, str) or not name.strip():
            return "Название не указано"
        return name

    @staticmethod
    def _validate_url(url: str) -> str:
        """Валидация URL вакансии."""
        print(f"Валидация url: {url}, type={type(url)}")
        if not url or not isinstance(url, str):
            raise ValueError(f"URL должен быть непустой строкой, получено: {url}, type={type(url)}")
        return url

    @staticmethod
    def _validate_salary(salary: Optional[dict | str]) -> str:
        """Валидация зарплаты."""
        print(f"Валидация salary: {salary}, type={type(salary)}")
        if not salary:
            return "Зарплата не указана"
        if isinstance(salary, str):
            return salary
        if not isinstance(salary, dict):
            return "Зарплата не указана"
        salary_from = salary.get('from')
        salary_to = salary.get('to')
        currency = salary.get('currency', 'RUR')

        if salary_from and salary_to:
            return f"{salary_from}-{salary_to} {currency}"
        elif salary_from:
            return f"от {salary_from} {currency}"
        elif salary_to:
            return f"до {salary_to} {currency}"
        return "Зарплата не указана"

    @staticmethod
    def _validate_description(description: Optional[str]) -> str:
        """Валидация описания."""
        print(f"Валидация description: {description}, type={type(description)}")
        if description is None or not isinstance(description, str):
            return "Описание не указано"
        if not description.strip():
            return "Описание не указано"
        cleaned = re.sub(r'<[^>]+>', '', description)
        return cleaned.strip() or "Описание не указано"

    @property
    def salary(self) -> str:
        return self._salary

    @property
    def name(self) -> str:
        return self._name

    def __lt__(self, other) -> bool:
        """Сравнение вакансий по зарплате."""
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только с объектом Vacancy")
        return self.parse_salary() < other.parse_salary()

    def parse_salary(self) -> float:
        """Парсинг зарплаты для сравнения."""
        if "не указана" in self._salary:
            return 0
        try:
            parts = self._salary.split()
            if '-' in parts[0]:
                salary_from, salary_to = map(float, parts[0].split('-'))
                return (salary_from + salary_to) / 2
            return float(parts[1]) if parts[0] in ['от', 'до'] else float(parts[0])
        except (ValueError, IndexError):
            return 0

    def to_dict(self) -> dict:
        """Преобразование вакансии в словарь."""
        return {
            'name': self._name,
            'alternate_url': self._url,
            'salary': self._salary,
            'snippet': {'requirement': self._description}
        }

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list['Vacancy']:
        """Преобразование списка словарей в список объектов Vacancy."""
        result = []
        for i, vacancy in enumerate(vacancies):
            name = vacancy.get('name', '')
            # Улучшенная обработка url
            url = vacancy.get('alternate_url')
            if url is None or (isinstance(url, str) and not url.strip()):
                url = vacancy.get('url', '')
                if url is None or (isinstance(url, str) and not url.strip()):
                    url = "URL не указан"
            salary = vacancy.get('salary')
            description = vacancy.get('snippet', {}).get('requirement') or \
                          vacancy.get('description', '')
            print(f"Обработка вакансии #{i}: данные={vacancy}, name={name}, url={url}, "
                  f"type(url)={type(url)}, salary={salary}, description={description}")
            try:
                obj = cls(name, url, salary, description)
                result.append(obj)
            except Exception as e:
                print(f"Ошибка при обработке вакансии #{i}: данные={vacancy}, "
                      f"тип ошибки={type(e).__name__}, сообщение={str(e)}")
                continue
        print(f"Результат cast_to_object_list: количество объектов={len(result)}")
        return result
