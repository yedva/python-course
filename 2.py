"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class DividedByZeroError(Exception):
    def __init__(self, text):
        self.text = text


a = input("Введите делимое: ")
b = input("Введите делитель: ")

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise DividedByZeroError("На ноль кто делит?")
    result = a / b
except ValueError:
    print("Не смог распознать числа")
except DividedByZeroError as err:
    print(err)
else:
    print(f"Результат деления: {result}")





