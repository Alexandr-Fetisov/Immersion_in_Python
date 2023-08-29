"""Задание №9 Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
- имена str
- ставка int
- премия str с указанием процентов вида «10.25%».
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии."""


def filling_array(n: int) -> list[str]:
    list_of_things = []
    for i in range(n):
        list_of_things.append(input(f"{i + 1}:"))
    return list_of_things


if __name__ == "__main__":
    # names=['Виктор', 'Михаил', 'Аня']
    # rate=[80000, 100000, 90000]
    # bonus = ['10%', '12%', '10%']

    LEN = int(input("Введите количество элементов : "))

    print("Введите Имена : ")
    names = filling_array(LEN)
    print("Введите Cтавку : ")
    rate_temp = filling_array(LEN)
    rate = [
        int(rate_temp[i]) if rate_temp[i].isdigit() else int((input(f"Введите число для ставки под номером{i + 1}:")))
        for i in range(LEN)]
    print("Введите Премию : ")
    bonus_temp = filling_array(LEN)
    bonus = [bonus_temp[i] + "%" for i in range(LEN)]

    dict_res = {names[i]: (rate[i] * float(bonus[i].split('%')[0]) / 100) for i in range(LEN)}

    print(dict_res)


