from typing import Optional, List


class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ('_name', '_url', '_salary', '_description')

    def __init__(self, name: str, url: str, salary: Optional[dict], description: str):
        self._name = self._validate_name(name)
        self._url = self._validate_url(url)
        self._salary = self._validate_salary(salary)
        self._description = self._validate_description(description)

    @staticmethod
    def _validate_name(name: str) -> str:
        """Валидация названия вакансии."""
        if not name or not isinstance(name, str):
            raise ValueError("Название вакансии должно быть непустой строкой")
        return name

    @staticmethod
    def _validate_url(url: str) -> str:
        """Валидация URL вакансии."""
        if not url or not isinstance(url, str):
            raise ValueError("URL должен быть непустой строкой")
        return url

    @staticmethod
    def _validate_salary(salary: Optional[dict]) -> str:
        """Валидация зарплаты."""
        if not salary or not isinstance(salary, dict):
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
    def _validate_description(description: str) -> str:
        """Валидация описания."""
        if not description or not isinstance(description, str):
            raise ValueError("Описание должно быть непустой строкой")
        return description

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
        return self._parse_salary() < other._parse_salary()

    def _parse_salary(self) -> float:
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
            'url': self._url,
            'salary': self._salary,
            'description': self._description
        }

    @classmethod
    def cast_to_object_list(cls, vacancies: List[dict]) -> List['Vacancy']:
        """Преобразование списка словарей в список объектов Vacancy."""
        result = []
        for vacancy in vacancies:
            name = vacancy.get('name', '')
            url = vacancy.get('alternate_url', '')
            salary = vacancy.get('salary')
            description = vacancy.get('snippet', {}).get('requirement', '')
            try:
                result.append(cls(name, url, salary, description))
            except ValueError:
                continue
        return result
