import json
import re
from module.abstract_classes import DatabaseOfVacancies


class JSONSaver(DatabaseOfVacancies):
    def __init__(self):
        self.__patch = 'file/vacancy.json'

    def add_vacancy(self, vacancy):
        """ Добавляет вакансию в json """

        all_entries = self.read_file_json()
        record_ids = [item.get('id') for item in all_entries]

        if vacancy.id in record_ids:
            return

        all_entries.append(vacancy.get_dict_vacancy())
        self.write_file_json(all_entries)

    def get_vacancies_by_salary(self, salary):
        """ Получает вакансию по зп форма записи должна быть 1000 - 10000 """

        # Поиск зп в строке
        salary = re.findall(r'\d+', salary)
        salary = [int(i) for i in salary]
        if len(salary) >= 3:
            raise InvalidFormat

        all_entries = self.read_file_json()
        for vacancy in all_entries:

            if len(salary) == 2:
                if salary[0] == vacancy['salary_from'] and salary[1] == vacancy['salary_to']:
                    return vacancy

            elif len(salary) == 1:
                if salary[0] == vacancy['salary_to']:
                    return vacancy

    def delete_vacancy(self, vacancy):
        """ Удаляет вакансию из json """

        all_entries = self.read_file_json()
        ids = [item['id'] for item in all_entries]
        vacancy_index = ids.index(vacancy.id)
        del all_entries[vacancy_index]
        self.write_file_json(all_entries)

    @staticmethod
    def read_file_json():
        """ Читает json """

        with open('file/vacancy.json', 'r', encoding='utf-8') as file:
            all_entries = json.load(file)
        return all_entries

    @staticmethod
    def write_file_json(all_entries):
        """ Записывает в json """

        with open('file/vacancy.json', 'w', encoding='utf-8') as file:
            json.dump(all_entries, file, indent=4)

    @property
    def patch(self):
        return self.__patch


class InvalidFormat(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Указан неверный формат'

    def __str__(self):
        return self.message
