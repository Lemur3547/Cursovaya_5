from src.classes import DBManager

with open('data/settings.txt', 'r+') as file:
    settings = file.read()
    if settings == '':
        file.write(input('Введите хост '))
        file.write('\n')
        file.write(input('Введите название базы данных '))
        file.write('\n')
        file.write(input('Введите имя пользователя '))
        file.write('\n')
        file.write(input('Введите пароль '))

while True:
    print('''\nЧто вы хотите сделать?
1. Подключиться к базе данных
2. Изменить параметры подключения
Для выхода из приложения введите exit''')
    case = input()
    if case == '1':
        print('Подключение...')
        with open('data/settings.txt', 'r') as file:
            settings = file.read().split('\n')
        database = DBManager(settings[0], settings[1], settings[2], settings[3])
        database.create_tables()
        print("Соединение установлено.")

        while True:
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
        with open('data/settings.txt', 'w') as file:
            file.write(input('Введите хост '))
            file.write('\n')
            file.write(input('Введите название базы данных '))
            file.write('\n')
            file.write(input('Введите имя пользователя '))
            file.write('\n')
            file.write(input('Введите пароль '))
        print("Данные обновлены.")
    elif case == 'exit':
        print('Выход...')
        break
    else:
        print('Неизвестная операция')



