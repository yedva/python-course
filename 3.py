"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.reverse()
    return sum(my_list[:2])


print(my_func(1, 2, 3))
