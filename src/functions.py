def set_config(file):
    """
    Функция для заполнения файла конфига данными
    :param file: Файл для записи
    """
    file.write('[postgresql]\n')
    file.write('host=' + input('Введите хост ') + '\n')
    file.write('database=' + input('Введите название базы данных ') + '\n')
    file.write('user=' + input('Введите имя пользователя ') + '\n')
    file.write('password=' + input('Введите пароль ') + '\n')


def presentation(rows):
    """
    Функция для вывода информации о вакансиях в консоль в удобном для восприятия виде
    :param rows: список вакансий
    """
    for row in rows:
        print(row[0])
        print(row[1])
        if row[2] is None and row[3] is None:
            print("Не указана")
        elif row[2] is None and row[3] is not None:
            print(f'До {row[3]} {row[4]}')
        elif row[2] is not None and row[3] is None:
            print(f'От {row[2]} {row[4]}')
        else:
            print(f'{row[2]} - {row[3]} {row[4]}')
        print(f"Ссылка на вакансию {row[5]}")
        print()