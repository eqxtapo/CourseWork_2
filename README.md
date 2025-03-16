# Интеграция с внешним сервисом

## Описание

В рамках проекта написана программа,
которая получает информацию о вакансиях с платформы hh.ru

## Установка:

1. Клонируйте репозиторий:

```
https://github.com/eqxtapo/CourseWork_2
```
## Конфигурация
1. Создайте виртуальное окружение poetry.

```
poetry env
```

2. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

3. Создайте файл .flake8 для настройки библиотеки


4. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 119
exclude = .git, __pycache__
```

Файл pyproject.toml

black, isort, mypy
```
[tool.black]
line_length = 119
exclude = '''
/(
  | \.git
)/
'''

[tool.isort]
line_length = 119

[tool.mypy]
disallow_untyped_defs = true
warn_return_any = true
exclude = '''
/(
  | \.venv
)/
'''
```

5. Установите библиотеку pandas, для работы с табличными данными.
Также, для корректной работы с Excel-файлами в pandas необходимо
дополнительно установить библиотеку openpyxl.
 
```
poetry add pandas
poetry add openpyxl
```

6. Установите библиотеки requests и dotenv
````commandline
poetry add requests
poetry add python-dotenv
````

## Тестирование

1. Для тестирования кода установите Pytest
```
poetry add --group dev pytest
```
2. Установите Code coverage для расчета процента протестированного кода
```
poetry add --group dev pytest-cov
```
Запуск Code coverage
```commandline
pytest --cov
```
Чтобы сгенерировать отчет о покрытии в HTML-формате, используйте следующую команду
```commandline
pytest --cov=src --cov-report=html
```
Отчет будет сгенерирован в папке
```
htmlcov
```
 и храниться в файле с названием 
```
index.html
```

3. Для тестирования вывода в консоль используйте специальную фикстуру
```
capsys
```

# Модули

## Модуль main.py
В модуле реализована основная работа по взаимодействию с пользователем. Создана функция взаимодействия с пользователем - main.

## Модуль file_worker.py

Содержит родительский абстрактный класс BaseFileReader(ABC) и его дочерний класс - JSONSaver.
В модуле реализован функционал для работы с API сервиса с вакансиями

## Модуль hh_api.py

Содержит родительский абстрактный класс BaseAPI(ABC) и его дочерний класс - HeadHunterAPI(BaseAPI).
В модуле реализован функционал по работе с файлами - чтение, запись в файл списка вакансий 

## Модуль utils.py

Содержит класс VacanciesFilterSort.
В модуле реализован функционал по работе со списком ваканский - фильтрации, сортировки и вывод топ вакансий

## Модуль vacancy.py

Содержит класс Vacancy.
В модуле реализован функционал для формирования вакансии
