def presentation(rows):
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