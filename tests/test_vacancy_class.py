from src.vacancy_class import Vacancy


def test_vacancy_init(first_vacancy):
    first_vacancy = Vacancy(first_vacancy)
    assert first_vacancy.name == "Python разработчик Middle/Senior в офис"
    assert first_vacancy.salary_from == 0
    assert first_vacancy.salary_to == 0
    assert first_vacancy.description == "Важная информация"
    assert first_vacancy.city == "Красноярск"
    assert first_vacancy.link == "https://krasnoyarsk.hh.ru/vacancy/118134197"

    assert (
        str(first_vacancy)
        == "Вакансия: Python разработчик Middle/Senior в офис, Зарплата: от 0 до 0, Описание: Важная информация, "
           "Город: Красноярск, "
        "Ссылка: https://krasnoyarsk.hh.ru/vacancy/118134197"
    )


def test_comparison(first_vacancy, second_vacancy):
    first_vacancy = Vacancy(first_vacancy)
    second_vacancy = Vacancy(second_vacancy)
    assert first_vacancy < second_vacancy
