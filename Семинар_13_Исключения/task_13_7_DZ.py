"""Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
"""
"""К задаче Создайте класс студента."""

import csv


class NameTypeError(Exception):
    def __init__(self, message):
        self.message = message


class VerificName:
    def check(self, value: str):
        if value != value.capitalize() or not value.isalpha():
            raise TypeError(
                'Первая буква должна быть заглавной! ФИО содержит только буквы!')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check(value)
        setattr(instance, self.name, value)


def lesson_from_csv():
    try:
        with open('lessons.csv', 'r', encoding='utf-8', newline='') as csv_f:
            csv_file = [*csv.reader(csv_f)]
            lesson = []
            grade = []
            test = []
            for i in range(1, len(csv_file)):
                lesson.append(csv_file[i][0])
                temp1 = csv_file[i][1].split()
                grade.append((sum(map(int, temp1))) / (len(temp1)))
                temp2 = csv_file[i][2].split()
                test.append((sum(map(int, temp2))) / (len(temp2)))

        for j in range(len(lesson)):
            print(f"Предмет: {lesson[j]} Средняя оценка: {grade[j]:.2f} Средний балл: {test[j]:.2f}")
        print(f"Средняя оценка: {sum(grade) / len(grade):.2f}  Средний балл: {sum(test) / len(test):.2f}")
    except FileNotFoundError:
        print("Файл 'lessons.csv' не найден!")
        # вывод информации если файл csv отсутствует


class Student:
    firstname = VerificName()
    patronymic = VerificName()
    name = VerificName()

    def __init__(self, firstname: str, name: str, patronymic: str):
        self.firstname = firstname
        self.patronymic = patronymic
        self.name = name

    def __repr__(self):
        return f"{self.firstname} {self.name} {self.patronymic}"


if __name__ == "__main__":
    try:
        stud = Student("Сидоров", "Пётр", "Иванович")
        # допустить ошибку в ФИО, например вместо буквы поставить цифру или символ
        print(repr(stud))
        lesson_from_csv()
    except NameTypeError as e:
        print(f"Ошибка при проверке имени: {e.message}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

