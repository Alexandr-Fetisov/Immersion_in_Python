"""
Задание №6
Погружение в Python | Коллекции
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
"""

texts = "vsdsdsdsdsds dfsfdf atdfdfd fdfdfd".split()
shift = len(max(texts))
for n, el in enumerate(sorted(texts), 1):
    print(f"{n}, {el:>{shift}}")