# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую
# структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм
# валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Store:
    computer = {}
    keyboard = {}
    printer = {}
    allproduct = []
    # def __init__(self):
    #     self.printer = {}
    #     self.computer = {}
    #     self.keyboard = {}
    #     self.allproduct = []


    def user_input(self):
        try:
            product_name = input("Введите название продукта: ")
            product_price = int(input("Введите стоимость: "))
            product_quantity = int(input("Ведите количество: "))
            product_type = input("Какой тип товара? Если принтер, ведите 1. Если компьютер, введите 2. "
                                 "Если клавиатура, введите 3: ")
            product = {"Наименование": product_name, "Стоимость": product_price, "Количество": product_quantity,
                       "Тип продукта": product_type}
            self.allproduct.append(product)
            if product_type == "1":
                self.printer.update(product)
            elif product_type == "2":
                self.computer.update(product)
            elif product_type == "3":
                self.keyboard.update(product)
        except:
            return "Некорректный ввод"
        user_exit = input("Для выхода введите stop. Для продолжения Enter: ")
        user_exit = user_exit.lower()
        if user_exit == "stop":
            print(f"Вся продукция: \n{self.allproduct}")
            return "Выходим"
        else:
            return Store.user_input(self)
class Printer(Store):
    def print(self):
        return f"В категории принтеры: {self.printer}"
class Computer(Store):
    def comp(self):
        return f"В категории компьютеры: {self.computer}"
class Keyboard(Store):
    def keyb(self):
        return f"В категории клавиатуры: {self.keyboard}"

product = Store()
print(product.user_input())
printer = Printer()
computer = Computer()
keyboard = Keyboard()
print(printer.print())
print(computer.comp())
print(keyboard.keyb())