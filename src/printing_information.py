
def print_vacancies(vacancies):
    for vacancy in vacancies:
        print('--------------------')
        salary = "Не указано"
        if vacancy.salary_to:
            salary = f"{vacancy.salary_from} - {vacancy.salary_to} руб." \
                if vacancy.salary_from else f"{vacancy.salary_to} руб."

        print(f"{vacancy.title}\nЗП: {salary}\n\n{vacancy.description}\n{vacancy.link}")
