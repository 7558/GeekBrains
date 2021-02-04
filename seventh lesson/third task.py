class Cell:
    def __init__(self, count):
        self.count = int(count)

    def __add__(self, other):
        return f"{self.count + other.count}"

    def __sub__(self, other):
        a = self.count - other.count
        return f"{a}" if a > 0 else "Пусто"

    def __mul__(self, other):
        return self.count * other.count

    def __truediv__(self, other):
        return self.count // other.count

    def make_order(self, param):
        result = ""
        for i in range(int(self.count / param)):
            result += "*" * param + "\n"
        result += "*" * (self.count % param) + "\n"
        return result

c = Cell(24)
b = Cell(2)
print(c + b)
print(c - b)
print(c / b)
print(c * b)
print(c.make_order(5))

