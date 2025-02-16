#Обработать файл csv: accident_base_pk.csv:
#1. Выбрать из файла явления "Сильный мороз" за период с 2019 по 2024 год с интенсивностью -33 и ниже и сохранить результат в отдельный файл.
import csv

with open(r'C:\Users\EmilA\OneDrive\Desktop\accident_base_pk.csv', 'r', encoding='utf-8') as pk:
    pk_data = csv.DictReader(pk, delimiter=',')
    pk_array = []
    for row in pk_data:
        if (row['accident_type'] == 'СИЛЬНЫЙ МОРОЗ' and
            2019 <= int(row['year']) <= 2024 and
            float(row['intensity']) <= -33):

            pk_array.append(row)

with open (r'C:\Users\EmilA\OneDrive\Desktop\sort_accident_base_pk.csv', 'w', encoding= 'utf-8') as sort_pk:
    writer_csv = csv.DictWriter(sort_pk, fieldnames=list(pk_array[0].keys()), lineterminator="\r")
    writer_csv.writeheader()
    for query_row in pk_array:
        writer_csv.writerow(query_row)
print(f'Всего {len(pk_array)} записей')