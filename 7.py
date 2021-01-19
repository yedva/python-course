"""
Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл,
вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [
    {“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
    {“average_profit”: 2000}
].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
from math import floor
import json

individual_profits = {}

with open('7.txt') as f:
    for line in f:
        line = line.strip().split(' ')
        # разделяем инфу с конца строки, т.к названия фирм могут быть с пробелами
        costs = int(line.pop())
        revenue = int(line.pop())
        entity_form = line.pop()
        name = ' '.join(line)
        individual_profits[name] = revenue - costs


profit_sum = sum([val for val in individual_profits.values() if val > 0])
avg_profit = {"average_profit": floor(profit_sum / len(individual_profits)) }

result_list = [
    individual_profits,
    avg_profit
]

print(result_list)

with open('7.json', 'w') as f:
    f.write(json.dumps(result_list, ensure_ascii=False))