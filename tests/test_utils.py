from src.utils import VacanciesFilterSort
from src.vacancy_class import Vacancy


def test_filter_init():
    test = VacanciesFilterSort(
        filter_word="python", filter_city="москва", filter_salary=[0, 1000], top_n=5
    )
    assert test.filter_word == "python"
    assert test.filter_city == "москва"
    assert test.filter_salary == [0, 1000]

    assert test.top_n == 5


def test_filter_by_description(vacancy_list, first_vacancy):
    test = VacanciesFilterSort(
        filter_word="информация", filter_city="Красноярск", filter_salary=[0, 0], top_n=5
    )
    assert test.filter_by_description(vacancy_list) == [Vacancy(first_vacancy)]


def test_filter_by_city(vacancy_list, second_vacancy):
    test = VacanciesFilterSort(
        filter_word="обязанности",
        filter_city="Земля",
        filter_salary=[10, 20],
        top_n=5,
    )
    assert test.filter_by_city(vacancy_list) == [Vacancy(second_vacancy)]


def test_filter_by_salary(vacancy_list, second_vacancy):
    test = VacanciesFilterSort(
        filter_word="обязанности", filter_city="Земля", filter_salary=[10, 20], top_n=5
    )
    assert test.filter_by_city(vacancy_list) == [Vacancy(second_vacancy)]


def test_sort_vacancies_by_salary(vacancy_list, first_vacancy, second_vacancy):
    test = VacanciesFilterSort(
        filter_word="обязанности", filter_city="Земля", filter_salary=[10, 20], top_n=5
    )
    assert test.sort_vacancies_by_salary(vacancy_list) == [
        Vacancy(second_vacancy),
        Vacancy(first_vacancy),
    ]


def test_get_top_vacancies(vacancy_list):
    test = VacanciesFilterSort(
        filter_word="", filter_city="", filter_salary=[0, 0], top_n=5
    )
    assert test.get_top_vacancies(vacancy_list) == (
        "Вакансия 1:\nВакансия: Python разработчик Middle/Senior в офис, Зарплата: от 0 до 0, Описание: Важная "
        "информация, Город: Красноярск, Ссылка: https://krasnoyarsk.hh.ru/vacancy/118134197\n\nВакансия 2:\nВакансия: "
        "Название второй вакансии, Зарплата: от 10 до 20, Описание: Какие-то обязанности, Город: Где-то на "
        "планете Земля, Ссылка: ссылка на вакансию\n\n"
    )
