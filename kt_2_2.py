#2. Выбрать из файла явления у которых был хоть какой-то ущерб (хранится в поле damage), т.е. где значения отличны от "нет данных", "нет ущерба" и т.п. и сохранить результат в отдельный файл.

import csv

with open(r'C:\Users\EmilA\OneDrive\Desktop\accident_base_pk.csv', 'r', encoding='utf-8') as pk:
    pk_data = csv.DictReader(pk, delimiter=',')
    pk_array = []

    for row in pk_data:
        if row['damage'].strip() not in ['НЕТ ДАННЫХ', 'НЕТ УЩЕРБА', 'БЕЗ УЩЕРБА', 'Без ущерба',
                                         'без ущерба', 'нет данных', 'Нет данных', 'НЕТ\xa0ДАННЫХ', 'Ущерба нет',
                                         'Данных об ущербе нет', 'Значительного ущерба нет',
                                         'Ущерба нет. Наблюдалось налипание мокрого снега диаметром 15 мм',
                                         'ущерба нет', 'Нет данных об ущербе']:
            pk_array.append(row)


with open (r'C:\Users\EmilA\OneDrive\Desktop\sort2_accident_base_pk.csv', 'w', encoding= 'utf-8') as sort_pk:
    writer_csv = csv.DictWriter(sort_pk, fieldnames=list(pk_array[0].keys()), lineterminator="\r")
    writer_csv.writeheader()
    for query_row in pk_array:
        writer_csv.writerow(query_row)
print(f'Всего {len(pk_array)} записей об ущербе')