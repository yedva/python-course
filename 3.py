"""
Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение.
Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание.
Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек
двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение.
Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление.
Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление
количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****...,
где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает,
то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.

Подсказка: подробный список операторов для перегрузки доступен по ссылке.
https://pythonworld.ru/osnovy/peregruzka-operatorov.html
"""


class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def make_order(self, columns):
        return ('*'*columns + '\n') * int(self.cell_num / columns) + '*' * (self.cell_num % columns)

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Cell object expected')
        return Cell(self.cell_num + other.cell_num)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Cell object expected')
        sub_result = self.cell_num - other.cell_num
        if sub_result > 0:
            return Cell(sub_result)
        else:
            raise Exception('not enough cells in first operand')

    def __mul__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Cell object expected')
        return Cell(self.cell_num * other.cell_num)

    def __truediv__(self, other):
        if not isinstance(other, Cell):
            raise TypeError('Cell object expected')
        return Cell(round(self.cell_num / other.cell_num))


c1 = Cell(12)
c2 = Cell(5)

add_cell = c1 + c2
print(add_cell.cell_num)

sub_cell = c1 - c2
print(sub_cell.cell_num)

mult_cell = c1 * c2
print(mult_cell.cell_num)

div_cell = c1 / c2
print(div_cell.cell_num)

print(c1.make_order(5))