from src.bulletin_board_API import HeadHunterAPI, SuperJobAPI
from src.file_saver import JSONSaver


def run_parser(search_query, platforms):
    """ Парсит вакансии и заносит в json, возвращает общий массив с экземплярами Vacancy """

    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    hh_vacancies = []
    superjob_vacancies = []

    # Получение вакансий с разных платформ
    if platforms == 1 or platforms == 3:
        hh_vacancies = hh_api.get_vacancies(search_query)
    if platforms == 2 or platforms == 3:
        superjob_vacancies = superjob_api.get_vacancies(search_query)

    # Слияние всех вакансий в один массив
    hh_vacancies.extend(superjob_vacancies)

    # Добавляет вакансии в json
    for vacancy in hh_vacancies:
        json_saver = JSONSaver()
        json_saver.add_vacancy(vacancy)
        json_saver.get_vacancies_by_salary("100000 - 150000 руб.")
        # json_saver.delete_vacancy(vacancy)

    return hh_vacancies
