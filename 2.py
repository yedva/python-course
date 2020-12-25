"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
user_seconds = int(input('Введите время в секундах: '))

hours = user_seconds // 3600
minutes = (user_seconds - (hours * 3600)) // 60
seconds = user_seconds - (hours * 3600) - (minutes * 60)

if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minutes = f'0{minutes}'
if seconds < 10:
    seconds = f'0{seconds}'

print(f'{hours}:{minutes}:{seconds}')
