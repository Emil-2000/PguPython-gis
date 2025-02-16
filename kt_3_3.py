import pandas as pd

# загрузка данных
file_path = r'C:\Users\EmilA\OneDrive\Desktop\kt_3_python\Занятие 13\wr88125.txt'

column_names = ['index', 'year', 'month', 'day', 'min_temp', 'avg_temp', 'max_temp', 'precipitation']
weather_data = pd.read_csv(file_path, sep=';', header=None, names=column_names)

# Удаление столбца 'index'
weather_data.drop(columns=['index'], inplace=True)

# Проверка наличия пропущенных значений
print("данные wr88125.txt:")
weather_data.info()
missing_values = weather_data.isnull().sum()
if missing_values.any():
    print("\nЕсть пропущенные значения в следующих столбцах:")
    print(missing_values[missing_values > 0])
else:
    print("\nПропущенных значений нет.")

#преобразование столбцов в числовой формат
weather_data['min_temp'] = pd.to_numeric(weather_data['min_temp'], errors='coerce')
weather_data['avg_temp'] = pd.to_numeric(weather_data['avg_temp'], errors='coerce')
weather_data['max_temp'] = pd.to_numeric(weather_data['max_temp'], errors='coerce')
weather_data['precipitation'] = pd.to_numeric(weather_data['precipitation'], errors='coerce')

#Объединение столбцов 'year', 'month' и 'day' в один столбец 'date'
weather_data['date'] = pd.to_datetime(weather_data[['year', 'month', 'day']])

# расчет размаха температур и количества предшествующих дней без осадков
def calculate_temp_and_days(td):
    td['temp_range'] = td['max_temp'] - td['min_temp']
    td['days_without_precipitation'] = td['precipitation'].eq(0).groupby(td['precipitation'].ne(0).cumsum()).cumsum()

#Вычисление среднегодовой температуры и общего количества осадков для каждого года
def calculate_stats(df):
    annual_avg_temp = df.groupby('year')['avg_temp'].mean()
    annual_total_precipitation = df.groupby('year')['precipitation'].sum()
    return annual_avg_temp, annual_total_precipitation

calculate_temp_and_days(weather_data)
avg_temp_series, total_precipitation_series = calculate_stats(weather_data)

print("\nСреднегодовая температура по годам:")
print(avg_temp_series)

print("\nОбщее количество осадков по годам:")
print(total_precipitation_series)