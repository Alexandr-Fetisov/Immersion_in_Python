"""
Задание №3
📌 Добавьте к задачам 1 и 2 строки документации для классов.
"""

"""
MyStr - class, наследует все возможности класса str
также имеет дополнительные атрибуты
"""

# для def __new__(cls, value, author_name):
"""
    Создает экземпляр класса с дополнительными атрибутами
    value: Переданная строка
    author_name: имя автора-создателя
    creation_time = datetime.datetime.now() - время создания
"""


"""
класс Archive хранит свойства:
число и строку, а также list-архивы предыдущих экземпляров класса.
При нового экземпляра класса, старые данные из ранее созданных экземпляров 
сохраняются в два списковархивов
"""

class Archive:
    '''Сохраняем данные каждого экземпляра класса в списки numbers и values.'''
    numbers = []
    values = []

    def __new__(cls, number: int, value: str):
        '''Переопределили метод new для сохранения аргументов в списки.'''
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance

    def __init__(self, number: int, value: str):
        '''Определили метод инициализации экземпляра класса.'''
        self.number = number
        self.value = value

    def __repr__(self):
        '''Переопределили метод выведения информации для разработчика'''
        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        '''Переопределили метод выведения строчного представления класса для пользователя'''
        return f'Номер: {self.number}, Значение: "{self.value}"'


if __name__ == '__main__':
    a_1 = Archive(1, "Один")
    # a_2 = Archive(2, "Два")
    # print(f'{a_1.numbers} {a_1.values}')
    # print(f'{a_2.numbers} {a_2.values}')
    # a_3 = Archive(3, "Три")
    # print(f'{a_3.numbers} {a_3.values}')
    # help(a_1)
    print(a_1.__repr__())
    print(f'{a_1 = }')
    print(a_1)