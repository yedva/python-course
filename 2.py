"""
Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""

some_list = []
some_list.extend(input('скажи любое слово, я перемешаю соседние буковки: '))

for i in range(len(some_list) // 2):
    a_ind = i * 2
    b_ind = a_ind + 1
    a_val, b_val = some_list[a_ind], some_list[b_ind]
    some_list[a_ind] = b_val
    some_list[b_ind] = a_val
print(''.join(some_list))
