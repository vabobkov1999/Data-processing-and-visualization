import pandas
import matplotlib.pyplot as plt
plt.style.use('ggplot')
FILE_PATH = 'API_AG.LND.FRST.K2_DS2_en_csv_v2_2058959.csv' # читаем файл
df = pandas.read_csv(FILE_PATH, skiprows=4) # выкидываем пустые и ненужные колонки
df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code', '2017', '2018', '2019', '2020'], axis=1, inplace=True, errors='ignore') # inplace=True разрешение конфликтов при копировании, axis=1 выкидываем построчно, errors игнорируем ошибки
print(df['Country Name'])
df.set_index('Country Name').sum().plot().set_title('Forest area (sq. km) from 1990 to 2016') # общий график по годам
df['Sum'] = df.sum(axis=1) # создаю столбик с суммой по каждой стране, с помощью него сортирую таблицу чтобы появился топ 5
print(df.sort_values('Sum', ascending=False))
country_list = df.sort_values('Sum', ascending=False)['Country Name'].head(5).tolist() # Дальше формирую список, который дальше использую в качестве локации откуда брать данные для второго графика
df.set_index('Country Name').loc[country_list].T.plot().set_title('Forest area (sq. km) in countries from 1990 to 2016')
plt.show()
