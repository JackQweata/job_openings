def filter_vacancies(vacancies, filter_words):
    """ Фильтрует вакансии по ключевым словам пользователя и площадки """

    filtered_vacancies = []

    if not filter_words:
        return vacancies

    for vacancy in vacancies:
        for word in filter_words:
            if vacancy.title.find(word) == -1:
                continue
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def sort_vacancies(vacancies):
    """ Сортирует вакансии по зп с большего меньшего """

    sorted_employees = sorted(vacancies,
                              key=lambda x: x.salary_to if x.salary_to is not None else float('inf'),
                              reverse=True
                              )
    return sorted_employees


def get_top_vacancies(vacancies, top_n):
    """ Ограничение на вывод вакансий  """

    if len(vacancies) < top_n:
        return vacancies
    return vacancies[:top_n]
