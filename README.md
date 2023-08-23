# "Погружение в Python"
### Семинар - 1 Основы Python:

*Задача_2_ДЗ:*

Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним. является ли этот день выходным.


*Задача_3_ДЗ:*

Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


*Задача_4_ДЗ:*

Решите квадратное уравнение 5x2-10x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
*Попробуйте решить уравнения с другими значениями a, b, c.


*Задача_5:*

Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.

*Задача_6:*

Напишите программу, которая запрашивает год и проверяет его на високосность.
Распишите все возможные проверки в цепочке elif
Откажитесь от магических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print

*Задача_7:*

Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print

*Задача_8:*

Нарисовать в консоли ёлку спросив у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5

*Задача_9:*

Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

### Семинар - 2 Простые типы данных:

*Задача_1:*

Создайте несколько переменных разных типов.Проверьте к какому типу относятся созданные переменные.

*Задача_2:*

Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:

- ✔ порядковый номер начиная с единицы
- ✔ значение
- ✔ адрес в памяти
- ✔ размер в памяти
- ✔ хэш объекта
- ✔ результат проверки на целое число только если он положительный
- ✔ результат проверки на строку только если он положительный

Добавьте в список повторяющиеся элементы и сравните на результаты.

*Задача_3:*

- ✔ Напишите программу, которая получает целое число и возвращает его двоичное, восьмеричное строковое представление.
- ✔ Функции bin и oct используйте для проверки своего результата, а не для решения.

Дополнительно:
- ✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
- ✔ Избегайте магических чисел
- ✔ Добавьте аннотацию типов где это возможно

*Задача_4_ДЗ:*

- ✔ Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
- ✔ Диаметр не превышает 1000 у.е.
- ✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

*Задача_5_ДЗ:*

- ✔ Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
- ✔ Используйте комплексные числа для извлечения квадратного корня.

*Задача_6:*

Напишите программу банкомат:
- ✔ Начальная сумма равна нулю
- ✔ Допустимые действия: пополнить, снять, выйти
- ✔ Сумма пополнения и снятия кратны 50 у.е.
- ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
- ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
- ✔ Нельзя снять больше, чем на счёте
- ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
- ✔ Любое действие выводит сумму денег

*Задача_7_1_ДЗ:*

Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex
используйте для проверки своего результата.

*Задача_7_2_ДЗ:*

Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
Программа должна возвращать сумму и *произведение дробей.
Для проверки своего кода используйте модуль fractions.

### Семинар - 3 Коллекции:

*Задача_1:*

- ✔ Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
- ✔ *Подготовьте два решения, короткое и длинное, которое не использует другие коллекции помимо списков.

*Задача_2:*

Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
- ✔ Целое положительное число
- ✔ Вещественное положительное или отрицательное число
- ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
- ✔ Строку в нижнем регистре в остальных случаях

*Задача_3:*

- ✔ Создайте вручную кортеж содержащий элементы разных типов.
- ✔ Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

*Задача_4:*

- ✔ Создайте вручную список с повторяющимися элементами.
- ✔ Удалите из него все элементы, которые встречаются дважды.

*Задача_5:*

- ✔ Создайте вручную список с повторяющимися целыми числами.
- ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
- ✔ Нумерация начинается с единицы.

*Задача_6:*

- ✔ Пользователь вводит строку текста.
- ✔ Вывести каждое слово с новой строки.
- ✔ Строки нумеруются начиная с единицы.
- ✔ Слова выводятся отсортированными согласно кодировки Unicode.
- ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова 
был один пробел между ним и номером строки.

*Задача_7:*

- ✔ Пользователь вводит строку текста.
- ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
- ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
- ✔ Обратите внимание на порядок ключей.
- ✔ Объясните почему они совпадают или не совпадают в ваших решениях.

*Задача_8_ДЗ:*

Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
- ✔ Какие вещи взяли все три друга
- ✔ Какие вещи уникальны, есть только у одного друга
- ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
- ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

*Задача_9_ДЗ:*

Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.

*Задача_10_ДЗ:*

В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

*Задача_11_ДЗ:*

Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.

### Семинар - 4 Функции:

*Задача_1:*

- ✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
- ✔ Строки нумеруются начиная с единицы.
- ✔ Слова выводятся отсортированными согласно кодировки Unicode.
- ✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

*Задача_2:*

- ✔ Напишите функцию, которая принимает строку текста.
- ✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

*Задача_3:*

- ✔ Функция получает на вход строку из двух чисел через пробел.
- ✔ Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
- ✔ Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

*Задача_4:*

- ✔ Функция получает на вход список чисел.
- ✔ Отсортируйте его элементы in place без использования встроенных в язык сортировок.
- ✔ Как вариант напишите сортировку пузырьком. Её описание есть в википедии.

*Задача_5:*

- ✔ Функция принимает на вход три списка одинаковой длины:
- - ✔ имена str,
- - ✔ ставка int,
- - ✔ премия str с указанием процентов вида «10.25%».
- ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
- ✔ Сумма рассчитывается как ставка умноженная на процент премии.

*Задача_6:*

- ✔ Функция получает на вход список чисел и два индекса.
- ✔ Вернуть сумму чисел между между переданными индексами.
- ✔ Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

*Задача_7:*

- ✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
- ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

*Задача_8:*

- ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
- ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
- ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

*Задача_9_ДЗ:*

Напишите функцию для транспонирования матрицы

*Задача_10_ДЗ:*

Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

*Задача_11_ДЗ:*

Возьмите задачу о банкомате из семинара 2.
- Разбейте её на отдельные операции — функции.
- Дополнительно сохраняйте все операции поступления и снятия средств в список.

### Семинар - 5 Итераторы и генераторы:

*Задача_5_1:*

Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”.

Сформируйте словарь, где:
- ✔второе и третье число являются ключами.
- ✔первое число является значением для первого ключа.
- ✔четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа.

*Задача_5_2:*

- ✔ Самостоятельно сохраните в переменной строку текста.
- ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
- ✔ Напишите преобразование в одну строку.

*Задача_5_3:*

Продолжаем развивать задачу 2.
- ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
- ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

*Задача_5_4:*

- ✔ Создайте генератор чётных чисел от нуля до 100.
- ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
- ✔ Решение в одну строку.

*Задача_5_5:*

- ✔ Напишите программу, которая выводит на экран числа от 1 до 100.
- ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
- ✔ Вместо чисел, кратных пяти — слово «Buzz».
- ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
- ✔ *Превратите решение в генераторное выражение.

*Задача_5_6:*

- ✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
- ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
- ✔ Для вывода результата используйте «принт» без перехода на новую строку.

*Задача_5_7:*

- ✔ Создайте функцию-генератор.
- ✔ Функция генерирует N простых чисел, начиная с числа 2.
- ✔ Для проверки числа на простоту используйте правило:
- «число является простым, если делится нацело только на единицу и на себя».

*Задача_5_8_ДЗ:*

Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.

*Задача_5_9_ДЗ:*

Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины:
- имена str
- ставка int
- премия str

с указанием процентов вида «10.25%».

В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии.

*Задача_5_10_ДЗ:*

Создайте функцию генератор чисел Фибоначчи (см. Википедию).

### Семинар - 6 Модули:

*Задача_6_1:*

Вспомните какие модули вы уже проходили на курсе.
Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами. (3-7 строк импорта).

*Задача_6_2:*

Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа:
- нижнюю и верхнюю границу и количество попыток.

Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

*Задача_6_3:*

Улучшаем задачу 2.

Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в
числовые параметры используйте генераторное выражение.

*Задача_6_4:*

Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами
отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана
загадка или ноль, если попытки исчерпаны.

*Задача_6_5:*

Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию,
чтобы передать ей все свои загадки.

*Задача_6_6:*

Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
и число (номер попытки, с которой она угадана).

Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания
из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.

*Задача_6_7:*

Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.

*Задача_6_8:*

- Создайте пакет с всеми модулями, которые вы создали за время занятия. 
- Добавьте в __init__ пакета имена модулей внутри дандер __all__. 
- В модулях создайте дандер __all__ и укажите только те функции, которые могут верно работать за пределами модуля.

*Задача_6_9_ДЗ:*

В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

*Задача_6_10_ДЗ:*

Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

*Задача_6_11_ДЗ:*

Напишите функцию в шахматный модуль.
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

### Семинар - 7 Файлы и файловая система:

*Задача_7_1:*

- ✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
- ✔ Первое число int, второе - float разделены вертикальной чертой.
- ✔ Минимальное число - -1000, максимальное - +1000.
- ✔ Количество строк и имя файла передаются как аргументы функции.

*Задача_7_2:*

- ✔ Напишите функцию, которая генерирует псевдоимена.
- ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
- ✔ Полученные имена сохраните в файл.

*Задача_7_3:*

- ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
- ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
- ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
- ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
- ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
- ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

*Задача_7_4:*

Создайте функцию, которая создаёт файлы с указанным расширением.

Функция принимает следующие параметры:
- ✔ расширение
- ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
- ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
- ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
- ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
- ✔ количество файлов, по умолчанию 42
- ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

*Задача_7_5:*

Доработаем предыдущую задачу.
- ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
- ✔ Расширения и количество файлов функция принимает в качестве параметров.
- ✔ Количество переданных расширений может быть любым.
- ✔ Количество файлов для каждого расширения различно.
- ✔ Внутри используйте вызов функции из прошлой задачи.

*Задача_7_6:*

Дорабатываем функции из предыдущих задач.
- ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
- ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
- ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

*Задача_7_7_ДЗ:*

- ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
- ✔ Каждая группа включает файлы с несколькими расширениями.
- ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

*Задача_7_8_ДЗ:*

Напишите функцию группового переименования файлов. Она должна:
- ✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
- ✔ принимать параметр количество цифр в порядковом номере.
- ✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
- ✔ принимать параметр расширение конечного файла.
- ✔ принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.

*Задача_7_9_ДЗ:*

Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами

### Семинар - 8 Сериализация:

*Задача_8_1:*

Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
- Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
- Имена пишите с большой буквы.
- Каждую пару сохраняйте с новой строки.

*Задача_8_2:*

Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
доступа (от 1 до 7).
- После каждого ввода добавляйте новую информацию в JSON файл.
- Пользователи группируются по уровню доступа.
- Идентификатор пользователя выступает ключём для имени.
- Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
- При перезапуске функции уже записанные в файл данные должны сохраняться.

*Задача_8_3:*

Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

*Задача_8_4:*

- Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
- Дополните id до 10 цифр незначащими нулями.
- В именах первую букву сделайте прописной.
- Добавьте поле хеш на основе имени и идентификатора.
- Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
- Имя исходного и конечного файлов передавайте как аргументы функции.

*Задача_8_5:*

Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
одноимённых pickle файлов.

*Задача_8_6:*

Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

*Задача_8_7:*

Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Распечатайте его как pickle строку.

*Задача_8_8_ДЗ:*

Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
- Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория.
- Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.

Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.

### Семинар - 9 Декораторы:

*Задача_9_1:*

Создайте функцию-замыкание, которая запрашивает два целых числа:
- от 1 до 100 для загадывания,
- от 1 до 10 для количества попыток

Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток. 

*Задача_9_2:*

Дорабатываем задачу 1.

Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюу-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.

*Задача_9_3:*

- Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
возвращает.
- При повторном вызове файл должен расширяться, а не перезаписываться.
- Каждый ключевой параметр сохраните как отдельный ключ json словаря.
- Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
- Имя файла должно совпадать с именем декорируемой функции.

*Задача_9_4:*

- Создайте декоратор с параметром.
- Параметр - целое число, количество запусков декорируемой функции.

*Задача_9_5:*

Объедините функции из прошлых задач.

Функцию угадайку задекорируйте:
- декораторами для сохранения параметров,
- декоратором контроля значений и
- декоратором для многократного запуска.

Выберите верный порядок декораторов.

*Задача_9_6:*

Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

*Задача_9_7_ДЗ:*

Напишите следующие функции:
- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

### Семинар - 10 ООП. Начало:

*Задача_10_1:*

- Создайте класс окружность.
- Класс должен принимать радиус окружности при создании экземпляра.
- У класса должно быть два метода, возвращающие длину окружности и её площадь.

*Задача_10_2:*

- Создайте класс прямоугольник.
- Класс должен принимать длину и ширину при создании экземпляра.
- У класса должно быть два метода, возвращающие периметр и площадь.
- Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

*Задача_10_3:*

- Напишите класс для хранения информации о человеке:

   ФИО, возраст и т.п. на ваш выбор.
- У класса должны быть методы:

  birthday для увеличения возраста на год

  full_name для вывода полного ФИО и т.п. на ваш выбор.
- Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

*Задача_10_4:*

- Создайте класс Сотрудник.
- Воспользуйтесь классом человека из прошлого задания.
- У сотрудника должен быть:

  шестизначный идентификационный номер

  уровень доступа вычисляемый как остаток от деления суммы цифр id на семь


*Задача_10_5:*

- Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
- У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
- Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

*Задача_10_6:*

- Доработайте задачу 5.
- Вынесите общие свойства и методы классов в класс Животное.
- Остальные классы наследуйте от него.
- Убедитесь, что в созданные ранее классы внесены правки.

*Задача_10_7_ДЗ:*

Доработаем задачи 5-6. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

*Задача_10_8_ДЗ:*

- Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
- Превратите функции в методы класса, а параметры в свойства.
- Задачи должны решаться через вызов методов экземпляра.

### Семинар - 11 ООП. Особенности Python:

*Задача_11_1:*

- 📌 Создайте класс Моя Строка, где:
- 📌 будут доступны все возможности str
- 📌 дополнительно хранятся имя автора строки и время создания (time.time)

*Задача_11_2:*

- 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
- 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков - архивов
- 📌 list-архивы также являются свойствами экземпляра

*Задача_11_3:*

- 📌 Добавьте к задачам 1 и 2 строки документации для классов.

*Задача_11_4:*

- 📌 Доработаем класс Архив из задачи 2.
- 📌 Добавьте методы представления экземпляра для программиста и для пользователя.

*Задача_11_5:*

- 📌 Дорабатываем класс прямоугольник из прошлого семинара.
- 📌 Добавьте возможность сложения и вычитания.
- 📌 При этом должен создаваться новый экземпляр прямоугольника.
- 📌 Складываем и вычитаем периметры, а не длинну и ширину.
- 📌 При вычитании не допускайте отрицательных значений.

*Задача_11_6:*

- 📌 Доработайте прошлую задачу.
- 📌 Добавьте сравнение прямоугольников по площади
- 📌 Должны работать все шесть операций сравнения

*Задача_11_7_ДЗ:*

- 📌 Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
- 📌Создайте класс Матрица. Добавьте методы для:
- cтрок документации и вывода на печать,
- сравнения,
- сложения,
- *умножения матриц

### Семинар - 12 ООП. Финал:

*Задача_12_1:*

- Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
- Экземпляр должен запоминать последние k значений.
- Параметр k передаётся при создании экземпляра.
- Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

*Задача_12_2:*

Доработаем задачу 1.
- Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

*Задача_12_3:*

- Создайте класс-генератор.
- Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
- Если переданы два параметра, считаем step=1.
- Если передан один параметр, также считаем start=1.

*Задача_12_4:*

- Доработайте класс прямоугольник из прошлых семинаров.
- Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
- Используйте декораторы свойств.

*Задача_12_5:*

- Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

*Задача_12_6:*

- Изменяем класс прямоугольника.
- Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

*Задача_12_7_ДЗ:*

Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых. 