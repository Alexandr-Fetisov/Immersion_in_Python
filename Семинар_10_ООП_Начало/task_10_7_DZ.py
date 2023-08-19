"""Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики."""


class Animal:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name


class Fish(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Мелководная", "Глубоководная")[self.feature > 500]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nГлубина: {self.feature}\nТип: {self.type}\n'


class Bird(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Небольшой размах", "Большой размах")[self.feature > 3]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nРазмах крыльев: {self.feature}\nТип: {self.type}\n'


class Mammals(Animal):
    def __init__(self, name, age, feature, type=None):
        super().__init__(name, age)
        self.feature = feature
        self.type = type or self.check_type()

    def check_type(self):
        return ("Мелкий", "Крупный")[self.feature > 100]

    def __str__(self):
        return f'Имя: {self.name}\nВозраст: {self.age}\nВес: {self.feature}\nТип: {self.type}\n'


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, age, feature, type=None):
        if animal_type == 'Fish':
            return Fish(name, age, feature, type)
        elif animal_type == 'Bird':
            return Bird(name, age, feature, type)
        elif animal_type == 'Mammals':
            return Mammals(name, age, feature, type)
        else:
            raise ValueError(f'Invalid animal type: {animal_type}')


if __name__ == '__main__':
    f = AnimalFactory.create_animal('Fish', 'Карась', 1, 20)
    b = AnimalFactory.create_animal('Bird', 'Каркуша', 2, 2)
    m = AnimalFactory.create_animal('Mammals', 'Михалыч', 12, 142)
    # Создаем экземпляр несуществующего класса, дабы убедиться, что будет ошибка по строке 69:
    # a = AnimalFactory.create_animal('Reptiles', 'Гена', 5, 100)

    print(f)
    print(b)
    print(m)
    # print(a)