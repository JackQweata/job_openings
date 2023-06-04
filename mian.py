from module.screening_vacancies import filter_vacancies, sort_vacancies, get_top_vacancies
from src.bulletin_board_API import HeadHunterAPI, SuperJobAPI
from src.file_saver import JSONSaver

hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("Python")
superjob_vacancies = superjob_api.get_vacancies("Python")
hh_vacancies.extend(superjob_vacancies)

for vacancy in hh_vacancies:
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    json_saver.get_vacancies_by_salary("100000 - 150000 руб.")
    # json_saver.delete_vacancy(vacancy)


def user_interaction():
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    platforms = int(input("Выберите платформу:\n 1) HeadHunter\n 2) SuperJob\n 3) Все\n"))
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filtered_vacancies = filter_vacancies(hh_vacancies, filter_words, platforms)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
