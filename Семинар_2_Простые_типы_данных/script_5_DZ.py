""" Задание №5
✔ Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
✔ Используйте комплексные числа для извлечения квадратного корня."""


a = float(input('Введите коэффициент а: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))

dis = b ** 2 - 4 * a * c

if dis >= 0:
    x1 = ((-1) * b + (dis ** 0.5)) / (2 * a)
    x2 = ((-1) * b - (dis ** 0.5)) / (2 * a)

else:
    x1 = complex(((-1) * b + (dis ** 0.5)) / (2 * a))
    x2 = complex(((-1) * b - (dis ** 0.5)) / (2 * a))

print(f'x1 = {x1}')
print(f'x2 = {x2}')