"""
Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

people_and_things: dict = {"Олег": ("спальник", "сало", "шампура", "спички", "фонарь", "воду"),
                           "Петя": ("спальник", "палатку", "картофель", "хлеб", "лук","воду"),
                           "Дима": ("спальник", "палатку", "сковороду", "топор","воду"),
                           "Вова": ("спальник", "палатку", "топор", "спирт","воду")
                           }

print(f'{", ".join(people_and_things)} отправились в поход.')

things_all_took = set()
all_things = set()
unique_thing = ''

for key in people_and_things:
    for element in people_and_things[key]:
        all_things.add(element)
print(f'Вещи, которые взяли друзья: {", ".join(all_things)}.\n')

for item in all_things:
    res = map(lambda x: item in x, people_and_things.values())
    if all(res):
        things_all_took.add(item)

    res = map(lambda x: x[0] if item in x[1] else None, people_and_things.items())
    res = filter(lambda x: True if x else False, res)
    res = list(res)
    if len(res) == 1:
        print(f'Только {res[0]} взял {item}.')

    res = map(lambda x: x[0] if item not in x[1] else None, people_and_things.items())
    res = filter(lambda x: True if x else False, res)
    res = list(res)
    if len(res) == 1:
        print(f'{res[0]} не брал {item}.')

print(f'\nКаждый взял с собой: {", ".join(things_all_took)}.')