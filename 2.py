"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothing(ABC):

    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def material_waste(self):
        pass


class Coat(Clothing):
    def __init__(self, name, size):
        self.type = 'coat'
        self.name = name
        self.__size = size

    @property
    def size(self):
        return self.__size

    @property
    def material_waste(self):
        return self.size/6.5 + 0.5


class Suit(Clothing):
    def __init__(self, name, height):
        self.type = 'suit'
        self.name = name
        self.__size = height

    @property
    def size(self):
        return self.__size

    @property
    def material_waste(self):
        return 2 * self.size + 0.3



def overall_material_waste(*kwargs):
    waste = 0
    for obj in kwargs:
        waste += obj.material_waste
    return waste


coat = Coat('Пальто для коней', 52)
print(coat.material_waste)

suit = Suit('Костюм прозрачный', 180)
print(suit.material_waste)

print(overall_material_waste(coat, suit))
