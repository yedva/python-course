"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__()
для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым
элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, *kwargs):
        self.matrix = []
        self.matrix.extend(kwargs)

    def __str__(self):
        result = ''
        for row in self.matrix:
            for col in row:
                result += f'{col} '
            result += '\n'
        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError('operands must be of Matrix type')
        sum_rows = []
        for row_index, a_row in enumerate(self.matrix):
            b_row = other.matrix[row_index]
            sum_row = [a_col + b_row[col_index] for col_index, a_col in enumerate(a_row)]
            sum_rows.append(sum_row)
        return Matrix(*sum_rows)


m = Matrix([1, 2, 3, 4], [2, 3, 4, 5])
m2 = Matrix([-1, -2, -3, -4], [-2, -3, -4, -5])
print(m, m2)

print(m + m2)
