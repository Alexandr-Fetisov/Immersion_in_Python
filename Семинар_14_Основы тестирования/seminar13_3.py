MIN_LEVEL = 5


class BaseException(Exception):
    pass


class LevelException(BaseException):
    def __init__(self, value, need_value):
        self.value = value
        self.need_value = need_value

    def __str__(self):
        return f"Ошибка уровня - level={self.value} меньше необходимого уровня)"


class AccessException(BaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Ошибка доступа'


if __name__ == '__main__':
    try:
        num = int(input('введите целое число:> '))
        if num < 1:
            raise AccessException(num)
        if num < MIN_LEVEL:
            raise LevelException(num, MIN_LEVEL)
    except LevelException as e:
        print(e)
    except AccessException as e:
        print(e)
    except ValueError as e:
        print(e)
    else:
        print('Доступ разрешен')