from src.classes import DBManager
from src.config import config
from src.functions import set_config

try:
    with open('data/database.ini', 'r+') as file:
        settings = file.read()
        if settings == '':
            set_config(file)
except IOError:
    with open('data/database.ini', 'w+') as file:
        set_config(file)




while True:
    print('''\nЧто вы хотите сделать?
1. Подключиться к базе данных
2. Изменить параметры подключения
Для выхода из приложения введите exit''')
    case = input()
    if case == '1':
        print('Подключение...')
        params = config('data/database.ini')
        try:
            database = DBManager(params)
            database.create_tables()
            is_connected = True
            print("Соединение установлено.")
        except UnicodeDecodeError:
            print("Ошибка при подключении к базе данных. Проверьте параметры подключения.")
            is_connected = False

        while is_connected:
            search = input("Введите ключевые слова для поиска ")
            print("Получение данных...")
            database.fill_db(search)
            print("Данные получены.")
            while True:
                print('1. Получить список компаний с количеством вакансий\n'
                      '2. Получить список вакансий\n'
                      '3. Получить среднюю зарплату по вакансиям\n'
                      '4. Получить список вакансий с зарплатой выше средней\n'
                      '5. Получить список вакансий по ключевому слову в названии\n'
                      '6. Новый поиск')
                case = input()
                if case == '1':
                    count = input("Введите количество компаний, которое хотите вывести или оставьте поле пустым "
                                  "для вывода всех компаний. ")
                    database.get_companies_and_vacancies_count(count)
                elif case == '2':
                    count = input("Введите количество вакансий, которое хотите вывести или оставьте поле пустым "
                                  "для вывода всех вакансий. ")
                    database.get_all_vacancies(count)
                elif case == '3':
                    database.get_avg_salary()
                elif case == '4':
                    count = input("Введите количество вакансий, которое хотите вывести или оставьте поле пустым "
                                  "для вывода всех вакансий. ")
                    database.get_vacancies_with_higher_salary(count)
                elif case == '5':
                    keyword = input("Введите ключевое слово для поиска ")
                    count = input("Введите количество вакансий, которое хотите вывести или оставьте поле пустым "
                                  "для вывода всех вакансий. ")
                    database.get_vacancies_with_keyword(keyword, count)
                elif case == '6':
                    break
                elif case == 'exit':
                    break
                else:
                    print('Неизвестная операция')
            if case == 'exit':
                break
        if case == 'exit':
            print('Выход...')
            break

    elif case == '2':
        with open('data/database.ini', 'w') as file:
            set_config(file)
        print("Данные обновлены.")

    elif case == 'exit':
        print('Выход...')
        break

    else:
        print('Неизвестная операция')
