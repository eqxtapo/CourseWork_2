import pytest

from src.vacancy_class import Vacancy


@pytest.fixture
def first_vacancy():
    return {
        "name": "Python разработчик Middle/Senior в офис",
        "alternate_url": "https://krasnoyarsk.hh.ru/vacancy/118134197",
        "salary": {"from": 0, "to": 0},
        "snippet": {"responsibility": "Важная информация"},
        "area": {
            "name": "Красноярск",
        },
    }


@pytest.fixture
def second_vacancy():
    return {
        "name": "Название второй вакансии",
        "alternate_url": "ссылка на вакансию",
        "salary": {"from": 10, "to": 20},
        "snippet": {"responsibility": "Какие-то обязанности"},
        "area": {
            "name": "Где-то на планете Земля",
        },
    }


@pytest.fixture
def vacancy_list(first_vacancy, second_vacancy):
    return [Vacancy(first_vacancy), Vacancy(second_vacancy)]
