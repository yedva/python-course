"""
Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class EquipmentStorage:

    def __init__(self):
        self.__items = {}

    def putin(self, item):
        if not self.__items.get(item.name):
            self.__items[item.name] = [item]
        else:
            self.__items[item.name].append(item)

    def rebase_item(self, name, department):
        named_items = self.__items.get(name)
        if len(named_items) > 0:
            named_items[0].change_department(department)

    def print_all_items(self):
        for name in self.__items.keys():
            for item in self.__items.get(name):
                print(f'{item.name} for {item.department}')


class OfficeEquipment:

    def __init__(self, name: str, department: str):
        self.name = name
        self.department = department

    def change_department(self, new_department):
        self.department = new_department


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


store = EquipmentStorage()

store.putin(Printer('Samsung P2', 'HR', 30))
store.putin(Printer('Samsung P2', 'DEVOPS', 30))



class QuantityError(Exception):
    pass


def new_printer():
    try:
        name = input('Название принтера: ')
        try:
            print_speed = int(input('Скорость печати: '))
            qty = int(input('Кол-во: '))
        except ValueError:
            raise QuantityError
    except QuantityError:
        print('Нужно число!')
    else:
        for i in range(qty):
            store.putin(Printer(name, 'Free', print_speed))
        store.print_all_items()


new_printer()