from module.screening_vacancies import filter_vacancies, sort_vacancies, get_top_vacancies
from module.parser_sites import run_parser
from src.printing_information import print_vacancies


def user_interaction():
    """ Взаимодействие с пользователем """

    search_query = input("Введите поисковый запрос: ")
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    platforms = int(input("Выберите платформу:\n 1) HeadHunter\n 2) SuperJob\n 3) Все\n"))
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # Парсим данные
    vacancies = run_parser(search_query, platforms)
    filtered_vacancies = filter_vacancies(vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
