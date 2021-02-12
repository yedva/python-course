"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class EquipmentStorage:

    def __init__(self):
        self.__items = []


class OfficeEquipment:

    def __init__(self, name: str, department: str):
        self.name = name
        self.department = department


class Printer(OfficeEquipment):

    def __init__(self, name: str, department: str, print_speed: int):
        OfficeEquipment.__init__(self, name, department)
        self.print_speed = print_speed


class Scanner(OfficeEquipment):

    def __init__(self, name: str, department: str, scan_speed: int):
        OfficeEquipment.__init__(self, name, department)
        self.scan_speed = scan_speed


class Xerox(OfficeEquipment):

    def __init__(self, name: str, department: str, copy_speed: int):
        OfficeEquipment.__init__(self, name, department)
        self.copy_speed = copy_speed

