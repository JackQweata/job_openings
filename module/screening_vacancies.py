def filter_vacancies(vacancies, filter_words, platform):
    platforms = ["HeadHunter", "SuperJob"]
    filter_platform = None if len(platforms) <= platform else platforms[platform-1]
    filtered_vacancies = []

    for vacancy in vacancies:
        for word in filter_words:
            if vacancy.title.find(word) == -1:
                continue

            elif not filter_platform:
                filtered_vacancies.append(vacancy)

            elif vacancy.platform == filter_platform:
                filtered_vacancies.append(vacancy)

    return filtered_vacancies


def sort_vacancies(vacancies):
    pass


def get_top_vacancies(vacancies, top_n):
    pass
