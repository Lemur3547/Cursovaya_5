import pytest

from src.classes import HeadHunterAPI, DBManager


@pytest.fixture
def hh_api():
    hh_api = HeadHunterAPI()
    return hh_api


def test_hh_api(hh_api):
    hh_api.get_vacancies('python', 0)


@pytest.fixture()
def db_manager():
    params = {'host': 'localhost', 'database': 'Cursovaya_4', 'user': 'postgres', 'password': 'Emik2507'}
    return DBManager(params)


def test_create_tables(db_manager):
    db_manager.create_tables()


def test_fill_db(db_manager):
    db_manager.fill_db('python')


def test_get_companies_and_vacancies_count(db_manager):
    db_manager.get_companies_and_vacancies_count('')
    db_manager.get_companies_and_vacancies_count('10')


def test_get_all_vacancies(db_manager):
    db_manager.get_all_vacancies('')
    db_manager.get_all_vacancies('10')


def test_get_avg_salary(db_manager):
    db_manager.get_avg_salary()
    db_manager.get_avg_salary()


def test_get_vacancies_with_higher_salary(db_manager):
    db_manager.get_vacancies_with_higher_salary('')
    db_manager.get_vacancies_with_higher_salary('10')


def test_get_vacancies_with_keyword(db_manager):
    db_manager.get_vacancies_with_keyword('python', '')
    db_manager.get_vacancies_with_keyword('java', '10')

    assert db_manager.get_vacancies_with_keyword('sdfgsdgdsfg', '') == print("По вашему запросу ничего не найдено.")
    assert db_manager.get_vacancies_with_keyword('sdfgsdfgsdfg', '10') == print("По вашему запросу ничего не найдено.")
