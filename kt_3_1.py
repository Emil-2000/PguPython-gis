# Задание 1.
#
# 1.	Прочитать данные из файла a.txt и преобразовать их в словарь (ключ – строкового типа, значение – целое).
# 2.	Занести данные из словаря в объект Series.
# 3.	Вывести данные на экран
# 4.	Отобразить столбиком только  фамилии учеников 8 класса
# 5.	«Перевести» всех учеников в следующий класс и вывести данные на экран
# 6.	Посчитать количество учеников в каждом классе и вывести данные на экран
# 7.	Вывести информацию об учениках с фамилиями Авдеев и Леонов.

import pandas as pd

# чтение данных из txt файла в словарь дата
data = {}
with open('C:\\Users\\EmilA\\OneDrive\\Desktop\\kt_3_python\\Занятие 13\\a.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            surname, class_num = parts
            data[surname] = int(class_num)

# занесение данных из словаря в объект Series
series = pd.Series(data)

print("Данные из Series:")
print(series)

# отображение только фамилий учеников 8 класса
print("\nФамилии учеников 8 класса:")
class_8_students = series[series == 8].index
for student in class_8_students:
    print(student)

# перевод учеников в следующий класс
series += 1
print("\nДанные после перевода в следующий класс:")
print(series)

# подсчет количества учеников в каждом классе
class_counts = series.value_counts()
print("\nКоличество учеников в каждом классе:")
print(class_counts)

# вывод об учениках с фамилиями Авдеев и Леонов
print("\nИнформация об учениках с фамилиями Авдеев и Леонов:")
students_info = series[['Avdeev', 'Leonov']]
print(students_info)
