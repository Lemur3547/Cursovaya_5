import builtins
from unittest import mock

import pytest

from src.functions import presentation, set_config


@pytest.fixture()
def rows():
    return [('Junior Software Engineer', 'Magis Corp', 500, 800, 'USD', 'https://hh.ru/vacancy/98427645'),
            ('Back End разработчик', 'ROBOUP', None, 4500000, 'UZS', 'https://hh.ru/vacancy/98654688'),
            ('Стажер-программист', 'Контора геймдева', 2500, None, 'BYR', 'https://hh.ru/vacancy/98346328'),
            ('Разработчик Python Junior', 'Казтелепорт', None, None, None, 'https://hh.ru/vacancy/98383317')]


def test_presentation(rows):
    assert presentation(rows) == print('''Junior Software Engineer
                                    Magis Corp
                                    500 - 800 USD
                                    Ссылка на вакансию https://hh.ru/vacancy/98427645
                                    
                                    Back End разработчик
                                    ROBOUP
                                    3000000.0 - 4500000.0 UZS
                                    Ссылка на вакансию https://hh.ru/vacancy/98654688
                                    
                                    Стажер-программист
                                    Контора геймдева
                                    От 2500 BYR
                                    Ссылка на вакансию https://hh.ru/vacancy/98346328
                                    
                                    Разработчик Python Junior
                                    Казтелепорт, АО
                                    Не указана
                                    Ссылка на вакансию https://hh.ru/vacancy/98383317
                                    ''')


def test_set_config():
    with open('test_database.ini', 'wt') as file:
        with mock.patch.object(builtins, 'input', lambda _: '1234'):
            set_config(file)

    with open('test_database.ini', 'rt') as file:
        assert file.read() == '''[postgresql]
host=1234
database=1234
user=1234
password=1234
'''
