"""
Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""

import csv


class Verific_name:
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


class Student:
    firstname = Verific_name()
    patronymic = Verific_name()
    name = Verific_name()

    def __init__(self, firstname: str, name: str, patronymic: str):
        self.firstname = firstname
        self.patronymic = patronymic
        self.name = name

    def __repr__(self):
        return f"{self.firstname} {self.name} {self.patronymic}"


if __name__ == "__main__":
    stud = Student("Сидоров", "Пётр", "Иванович")
    print(repr(stud))
    lesson_from_csv()
