"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def collect_user_input():
    while True:
        user_input = input('Введите что-нибудь: ')
        if user_input:
            yield user_input
        else:
            break


user_lines = [line + '\n' for line in collect_user_input()]  # собираем строчки от юзера сюда


if len(user_lines) > 0:
    with open('1.txt', 'a') as f:
        f.writelines(user_lines)
