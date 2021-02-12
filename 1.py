"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
import re
from exeptions_1 import InvalidDay, InvalidMonth, InvalidYear


class Date:
    def __init__(self, date_string: str):
        day, month, year = Date.parse(date_string)
        Date.validate(day, month, year)
        self._day = day
        self._month = month
        self._year = year

    @classmethod
    def parse(cls, date_string: str):
        return [*map(int, re.split('\D', date_string))]

    @staticmethod
    def validate(day: int, month: int, year: int):
        if day < 1 or day > 31:
            raise InvalidDay

        if month < 1 or month > 12:
            raise InvalidMonth

        if year < 1:
            raise InvalidYear

    @property
    def day(self):
        return self._day

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year



try:
    today = Date('5-2-2021')
except InvalidDay:
    print('Не бывает таких дней')
except InvalidMonth:
    print('Нет таких месяцев')
except InvalidYear:
    print('Работаем только по нашей эре')
else:
    print(f'День: {today.day}, Месяц: {today.month}, Год: {today.year}')
