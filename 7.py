"""
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и
умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""

class Complex():
    def __init__(self, real, j):
        self.real = real
        self.j = j

    def __add__(self, other):
        return Complex(self.real + other.real, self.j + other.j)

    def __mul__(self, other):
        real = self.real * other.real - self.j * other.j
        j = self.j * other.real + self.real * other.j
        return Complex(real, j)

    def __str__(self):
        return f'{self.real} {"+" if self.j >= 0 else "-"} {abs(self.j)}j'

print(complex(2, 4) + complex(3, -5), complex(2, 4) * complex(3, -5))

cplx1 = Complex(2, 4)
cplx2 = Complex(3, -5)
print(cplx1 + cplx2, cplx1 * cplx2)

