# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
# PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите
# результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехал"

    def stop(self):
        return f"{self.name} остановилась"

    def turn(self, count):
        if count == "право":
            return f"{self.name} повернул направо"
        elif count == "лево":
            return f"{self.name} повернул налево"
    def show_speed(self):
        return f"Текущая скорость {self.name} - {self.speed}"

    def police(self):
        if self.is_police:
            return f"{self.name} полицейская машина"
        else:
            return f"{self.name} не полицейская машина"

class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name} - {self.speed}")
        if self.speed > 60:
            return f"{self.name} превышает скорость!"

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name} - {self.speed}")
        if self.speed > 40:
            return f"{self.name} превышение скорости!"

class Police(Car):
    pass

vaz = TownCar(100, "Зеленая", "Ваз", True)
kamaz = SportCar(300, "Черная", "Камаз", False)
rr = WorkCar(30, "Белая", "Ренж", False)
vw = Police(50, "Синяя", "Фольц", True)

print(vaz.turn("право"))
print(f"{kamaz.name} движется со скоростью:\n{kamaz.show_speed()}")
print(f"{rr.go()}")
print(f"{vw.police()}")
print(f"{rr.police()}")
print(vaz.show_speed())
print(rr.show_speed())