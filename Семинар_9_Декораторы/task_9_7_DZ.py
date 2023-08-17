"""Напишите следующие функции:
- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса"""

import csv
import random
from functools import wraps
from task_9_3 import decor
import shutil
import os

START_NUM, END_NUM = 1, 100


def generate_csv_file(filename, rows):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for _ in range(rows):
            row = [random.randint(START_NUM, END_NUM) for _ in range(3)]
            writer.writerow(row)


def solve_quadratic_equation_with_csv(func):
    wraps(func)

    def wrapper(filename):
        with open(filename, "r", encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Уравнение: {a}x\u00B2 + {b}x + {c} = 0")
                print(f"Корни: {result}")
                print()

    return wrapper


@solve_quadratic_equation_with_csv
@decor
def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root,
    else:
        return 'Нет рациональных корней'


if __name__ == '__main__':
    # Генерация CSV файла
    generate_csv_file("numbers.csv", 100)

    # Решение квадратного уравнения с каждой тройкой чисел из CSV файла
    solve_quadratic_equation("numbers.csv")

# Создание временной папки для хранения игр
os.makedirs("games")

# Копирование файлов игр в временную папку
shutil.copy("task_9_5.py", "games/task_9_5.py")
shutil.copy("task_9_6.py", "games/task_9_6.py")

# Архивирование игр в пакет
shutil.make_archive("games_package", "zip", "games")

# Удаление временной папки
shutil.rmtree("games")
