# Реализовать функцию my_func(), которая принимает
# три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    """Собираем в список и выводим максимум из списка."""
    numbers = []
    numbers.append(num1)
    numbers.append(num2)
    numbers.append(num3)
    max1 = (max(numbers))
    numbers.remove(max1)
    max2 = int((max(numbers)))
    max1 = int(max1)
    return print(max1 + max2)


print("Программа выводит максимальное значение.")
num1 = input("Введите первое значение: ")
num2 = input("Введите второе значение: ")
num3 = input("Введите третье значение: ")

my_func(num1, num2, num3)