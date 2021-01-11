"""
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""


def print_form(
        first_name='',
        last_name='',
        birth_date='',
        birthplace='',
        mail='',
        phone=''
):
    print(f'\n{first_name} {last_name}, род. {birth_date} в {birthplace}, почта {mail}, номер {phone}')


print_form(
    first_name=input('Ваше имя: '),
    last_name=input('Фамилия: '),
    birth_date=input('Дата рождения: '),
    birthplace=input('Место рождения: '),
    mail=input('Почта: '),
    phone=input('Телефон: '),
)
