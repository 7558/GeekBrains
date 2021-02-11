# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и
# выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"{self.a + other.a} + {self.b + other.b}i"

    def __mul__(self, other):
        return f"{self.a * other.a - (self.b * other.b)} + {self.b * other.a}i"

    def __str__(self):
        return f"{self.a} + {self.b}i"

a_1 = Complex(1, 2)
a_2 = Complex(4, 6)
print(a_1)
print(a_1 + a_2)
print(a_1 * a_2)