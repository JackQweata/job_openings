class Vacancy:
    def __init__(self, vacancy_id, title, link, description, agreement, salary_from, salary_to, platform):
        self.__id = vacancy_id
        self.__platform = platform
        self.__title = title
        self.__link = link
        self.__description = description
        self.__agreement = agreement
        self.__salary_from = salary_from
        self.__salary_to = salary_to

    def get_dict_vacancy(self):
        dict_vacancy = {
            "id": self.id,
            "platform": self.platform,
            "title": self.title,
            "link": self.link,
            "description": self.description,
            "agreement": self.agreement,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to
        }
        return dict_vacancy

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def link(self):
        return self.__link

    @property
    def description(self):
        return self.__description

    @property
    def agreement(self):
        return self.__agreement

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def platform(self):
        return self.__platform

    def __str__(self):
        return self.__title

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__title, self.__agreement})"

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise TypeError('Класс не явятся Vacancy')
        return self.salary_to == other.salary_to and self.agreement == other.agreement
