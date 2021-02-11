#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day):
        self.day = day

    @classmethod
    def extract(cls, day):
        list_day = []
        for i in day.split():
            list_day.append(i)
        return int(list_day[0]), int(list_day[1]), int(list_day[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return  "Все ок"
                else:
                    return "Неправильный год"
            else:
                return "Нерпавильный месяц"
        else:
            return "Неправильный день"

    def __str__(self):
        return f"Дата {Data.extract(self.day)}"

day = Data("01  01  2020")
print(day)
print(day.valid(20, 12, 2040))

