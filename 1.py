"""
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def divide(a, b):
    result = 0
    if a > 0 and b > 0:
        result = a / b
    return result


def ask_number(text):
    user_input = input(text)
    if user_input.isnumeric():
        return int(user_input)
    else:
        return ask_number(f'{user_input} не число, попробуйте еще раз: ')


def main():
    a = ask_number('Введите делимое: ')
    b = ask_number('Введите делитель: ')

    print(f'Частное: {divide(a, b)}\n')
    main()


main()
