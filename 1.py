"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from enum import Enum
from time import sleep
from sys import exit


class TrafficLightModes(Enum):
    STOP = {'color': 'red', 'duration': 7, 'order': 0}
    STEADY = {'color': 'yellow', 'duration': 2, 'order': 1}
    START = {'color': 'green', 'duration': 10, 'order': 2}


class TrafficLight:
    __color = (
        TrafficLightModes.STOP,
        TrafficLightModes.STEADY,
        TrafficLightModes.START,
    )

    def running(self, break_traffic_light=False):
        if break_traffic_light:  # ломаем светофор
            self.__color = (
                TrafficLightModes.START,
                TrafficLightModes.STOP,
                TrafficLightModes.STEADY,
            )
        self.check_colors_order()  # проверяем порядок огней
        for color in self.__color:
            print(color.value.get('color'))
            sleep(color.value.get('duration'))  # пауза

    def check_colors_order(self):
        current_order = [color.value.get('order') for color in self.__color]
        if current_order != sorted(current_order):
            print('Traffic light is broken!')
            exit()


tl = TrafficLight()

tl.running()
tl.running(break_traffic_light=True)
