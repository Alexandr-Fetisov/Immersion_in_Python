"""- На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
- Напишите аналогичный декоратор, но внутри используйте модуль logging."""

# вариант 1

import logging
from typing import Callable

logging.basicConfig(level=logging.INFO, filename='task2.log', encoding='utf-8')
logger = logging.getLogger(__name__)


def deco_func(func: Callable):
    def wrapper(*args, **kwargs):
        dct = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        dct['result'] = result
        logger.info(dct)

        return result

    return wrapper


@deco_func
def any_name(num: int, *args, **kwargs):
    return num ** 2


if __name__ == '__main__':
    any_name(15, 25, 'Привет', name='Александр', x=3, y=True)

# вариант 2
import random

logging.basicConfig(filename='task2.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def one(func):  # декоратор на функцию three
    def two(*args, **kwargs):
        rezult = func(*args)
        logger.info(f'Аргументы функции: {args}, результат: {rezult}')
        return rezult

    return two


@one
def three(a, b):
    return a + b


if __name__ == '__main__':
    print(three(random.randint(1, 11), random.randint(1, 11)))
