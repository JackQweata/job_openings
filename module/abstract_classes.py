from abc import abstractmethod
from fake_headers import Headers


class DatabaseOfVacancies:
    @abstractmethod
    def add_vacancy(self, vacancy):
        """ Добавить запись """

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        """ Получить ваксию по ЗП """

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """ Удаления вакансии """


class VacancyAPI:
    def __init__(self):
        self.headers = Headers(headers=True)

    @abstractmethod
    def get_vacancies(self, text):
        """ Получить вакансии через API """
