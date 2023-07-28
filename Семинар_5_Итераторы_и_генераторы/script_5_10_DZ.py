"""Задание №10 Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


print(*fibonacci(10))
