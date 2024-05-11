import pytest

from src.functions import presentation


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
