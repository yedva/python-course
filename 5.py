"""
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

numbers = [0, 1, 214, 23, 214, 55, 2]

with open('5.txt', 'w') as f:
    f.write(' '.join(map(str, numbers)))

with open('5.txt', 'r') as f:
    nums = f.read()
    sum_nums = sum(map(int, nums.split(' ')))

print(sum_nums)