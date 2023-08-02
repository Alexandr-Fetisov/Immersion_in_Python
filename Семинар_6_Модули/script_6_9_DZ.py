"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

from script_6_7 import dat

def imput_date()->str:
    date=input('Введите дату в формате DD.MM.YYYY: ')
    return date

if __name__=="__main__":
    print(dat(imput_date()))