"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('riding')

    def stop(self):
        print('stopping')

    def turn(self, direction):
        print(f'turning to the {direction}')

    def show_speed(self):
        print(f'speed is {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('speeding detected')
        else:
            super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('speeding detected')
        else:
            super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


lamborghini = SportCar(340, 'yellow', 'Lamborghini Aventador', False)
print(f'\n{lamborghini.name}')
lamborghini.show_speed()
lamborghini.go()
lamborghini.turn('right')
lamborghini.stop()

explorer = PoliceCar(220, 'white', 'Ford Explorer')
print(f'\n{explorer.name} {"is" if explorer.is_police else "is not"} a police car')
explorer.show_speed()
explorer.go()
explorer.turn('left')
explorer.stop()

camry = TownCar(250, 'black', 'Toyota Camry', False)
print(f'\n{camry.name}')
camry.go()
camry.show_speed()

volvo = WorkCar(30, 'red', 'Volvo Truck', False)
print(f'\n{volvo.name}')
volvo.go()
volvo.show_speed()

