import os
import requests
from module.abstract_classes import VacancyAPI
from module.vacancy import Vacancy


class HeadHunterAPI(VacancyAPI):
    def __init__(self):
        super().__init__()

    def get_vacancies(self, text):
        """ Получение вакансий HeadHunter через API, возвращает массив экземпляров класса  Vacancy"""

        try:
            vacancies_api = requests.get(f'https://api.hh.ru/vacancies/?text={text}', headers=self.headers.generate())
            vacancies_api = vacancies_api.json().get('items')

            vacancies = [Vacancy(
                vacancy_id=int(vacancy['id']),
                title=vacancy['name'],
                link=vacancy['alternate_url'],
                description=vacancy['snippet']['responsibility'],
                agreement=vacancy['salary']['gross'] if vacancy.get('salary') else None,
                salary_from=vacancy['salary']['from'] if vacancy.get('salary') else None,
                salary_to=vacancy['salary']['to'] if vacancy.get('salary') else None,
                platform='HeadHunter'
            )
                for vacancy in vacancies_api]

            return vacancies

        except Exception as __err:
            print(f"[ERROR] {__err}")


class SuperJobAPI(VacancyAPI):
    def __init__(self):
        super().__init__()
        self.__TOKEN = os.getenv('KEY_SUPER_JOB')

    def get_vacancies(self, text):
        """ Получение вакансий SuperJob через API, возвращает массив экземпляров класса  Vacancy"""

        header = self.headers.generate()
        header['X-Api-App-Id'] = self.__TOKEN
        try:
            vacancies_api = requests.get(f'https://api.superjob.ru/2.0/vacancies/?keyword={text}', headers=header)
            vacancies_api = vacancies_api.json().get('objects')

            vacancies = [Vacancy(
                vacancy_id=int(vacancy['id']),
                title=vacancy['profession'],
                link=vacancy['link'],
                description=vacancy['candidat'],
                agreement=vacancy['agreement'],
                salary_from=vacancy['payment_from'],
                salary_to=vacancy['payment_to'],
                platform='SuperJob'
            )
                for vacancy in vacancies_api]

            return vacancies

        except Exception as __err:
            print(f"[ERROR] {__err}")
