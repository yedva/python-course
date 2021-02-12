"""
Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
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

store.print_all_items()

store.rebase_item('Samsung P2', 'Reception')
print('\n')
store.print_all_items()
