from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.ratio('Привет мир', 'Привет мир')
print(a)
#Выводит в консоль: 100

a = fuzz.ratio('Привет мир', 'Привт кир')
print(a)
#Выводит в консоль: 84

a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)
#Выводит в консоль: 100

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, Привет мир')
print(a)
#Выводит в консоль: 100

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, привет мир')
print(a) 
#Выводит в консоль: 90

a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(a)
#Выводит в консоль: 100

a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш любимый Привет')
print(a)
#Выводит в консоль: 78

a = fuzz.token_sort_ratio('1 2 Привет наш мир', '1 мир наш 2 ПриВЕт')
print(a)
#Выводит в консоль: 100

a = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
print(a)
#Выводит в консоль: 100

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(a)
#Выводит в консоль: 100

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт, наш мир!')
print(a)
#Выводит в консоль: 97

city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extract("Саратов", city, limit=2)
# Параметр limit по умолчанию имеет значение 5
print(a)
#Выводит в консоль: [('Саратов', 100), ('Самара', 62)]

city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extractOne("Краногрск", city)
print(a)
#Выводит в консоль: ('Красногорск', 90)

