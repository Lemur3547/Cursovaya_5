import json
from abc import ABC, abstractmethod

import psycopg2
import requests


class APIVacancies(ABC):
    @abstractmethod
    def get_vacancies(self, name, page):
        pass


class HeadHunterAPI(APIVacancies):
    def __init__(self):
        self.hh_api = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, name, page):
        response = requests.get(self.hh_api, params={'text': name, 'per_page': 100, 'page': page})
        vacancies = response.json()
        with open('data/vacancies.json', 'wt', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False)


class DBManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def create_tables(self):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                cur.execute('drop table if exists vacancies')

                cur.execute("""create table vacancies
                            (
                                vacancy_id int primary key,
                                vacancy_name varchar(100),
                                city varchar(50),
                                salary_from float,
                                salary_to float,
                                salary_currency varchar(3),
                                vacancy_type varchar(10),
                                address varchar(256),
                                url text,
                                employer_name varchar(256),
                                requirement text,
                                responsibility text,
                                contacts text,
                                schedule varchar(20),
                                professional_roles_name varchar(60),
                                experience varchar(20),
                                employment varchar(20)
                            )""")
        conn.close()

    def fill_db(self, keyword):
        with psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password) as conn:
            with conn.cursor() as cur:
                HH_api = HeadHunterAPI()
                for page in range(20):
                    # try:
                    HH_api.get_vacancies(keyword, page)
                    # except requests.exceptions.ConnectTimeout:
                    #     print("Ошибка")

                    with open("data/vacancies.json", 'rt', encoding='utf-8') as file:
                        vacancies_list = json.load(file)

                    for vacancy in vacancies_list["items"]:
                        # cur.execute('insert into employers values(%s, %s)',
                        #             (vacancy["employer"]["id"], vacancy["employer"]["name"]))
                        #
                        # cur.execute('insert into professional_roles values(%s, %s)',
                        #             (vacancy["professional_roles"][0]["id"],
                        #              vacancy["professional_roles"][0]["name"]))

                        cur.execute('insert into vacancies ('
                                    'vacancy_id'
                                    ', vacancy_name'
                                    ', city'
                                    ', vacancy_type'
                                    ', url'
                                    ', employer_name'
                                    ', requirement'
                                    ', responsibility'
                                    ', contacts'
                                    ', schedule'
                                    ', professional_roles_name'
                                    ', experience'
                                    ', employment'
                                    ') values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                    (vacancy["id"]
                                     , vacancy["name"]
                                     , vacancy["area"]["name"]
                                     , vacancy["type"]["name"]
                                     , vacancy["alternate_url"]
                                     , vacancy["employer"]["name"]
                                     , vacancy["snippet"]["requirement"]
                                     , vacancy["snippet"]["responsibility"]
                                     , vacancy["contacts"]
                                     , vacancy["schedule"]["name"]
                                     , vacancy["professional_roles"][0]["name"]
                                     , vacancy["experience"]["name"]
                                     , vacancy["employment"]["name"]
                                     ))
                        if vacancy["salary"] is not None:
                            cur.execute('update vacancies set salary_from = %s, salary_to = %s, '
                                        'salary_currency = %s where vacancy_id = %s',
                                        (vacancy["salary"]["from"]
                                         , vacancy["salary"]["to"]
                                         , vacancy["salary"]["currency"]
                                         , vacancy["id"]))

                        if vacancy["address"] is not None:
                            cur.execute('update vacancies set address = %s where vacancy_id = %s',
                                        (vacancy["address"]["raw"]
                                         , vacancy["id"]))




