import requests
import pandas
import matplotlib.pyplot as mpl

url = "https://catfact.ninja/fact"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Факт о кошках:", data['fact'])
else:
    print("Ошибка:", response.status_code)



data_frame = pandas.read_csv('data.csv')
print("Базовая статистика данных:\n", data_frame.describe())
avg_values = data_frame.groupby('Category')['Value'].mean()
print("Средние значения по категориям:\n", avg_values)


x = [1,3,5,6,7,8]
y = [2,5,6,7,8,9]

mpl.plot(x,y)
mpl.xlabel('X')
mpl.ylabel('Y')
mpl.title('Линейный график')
mpl.show()


