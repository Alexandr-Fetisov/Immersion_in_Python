# 3. Создайте класс с базовым исключением и дочерние классы-исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class BaseException(Exception):
    pass

class LevelException(BaseException):
    def __init__(self, level, name):
        self.level = level
        self.name = name
    def __str__(self):
        return f'Level {self.level} incorrect for user {self.name}!'


class AccessException(BaseException):
    def __init__(self, user_id):
        self.user_id = user_id
    def __str__(self):
        return f'Access for {self.user_id} denied!'


"""class BaseException(Exception):
    pass


class LevelException(BaseException):
    def __str__(self) -> str:
        return "Ошибка уровня"


class AccessException(BaseException):
    def __str__(self) -> str:
        return 'Ошибка доступа'


if __name__ == '__main__':
    raise LevelException"""



"""class My_Exception(Exception):
    def __init__(self, value):
        self.value = value


class Level_Ecception(My_Exception):
    def __str__(self):
        return f'Произошла ошибка уровня. {self.value}: такой уровень не найден.'


class Access_Exception(My_Exception):
    def __str__(self):
        return f'Не верный уровень доступа.'


if __name__ == '__main__':
    raise Level_Ecception(4)"""

