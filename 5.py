"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start rendering...')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} is drawing like a pen')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} is drawing like a pencil')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'{self.title} is drawing like a handle')


parker = Pen('Parker')
parker.draw()

papermate = Pencil('Papermate')
papermate.draw()

attache = Handle('Attache')
attache.draw()
