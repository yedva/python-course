"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def format_line(line):
    return {
        'last_name': line[0],
        'wage': int(line[1])
    }


employees = list(map(format_line, [line.strip().split(',') for line in open('3.txt', 'r')]))

print('Сотрудники с зп меньше 20000:')
for employee_with_wage_lt_20k in filter(lambda e: e['wage'] < 20000, employees):
    print(employee_with_wage_lt_20k['last_name'])

wage_sum = sum(map(lambda e: e['wage'], employees))
print(f'Средний доход всех сотрудников {wage_sum / len(employees)}')
