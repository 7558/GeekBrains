# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Division:
    @staticmethod
    def divide(number_one, number_two):
        try:
            return number_one / number_two
        except ZeroDivisionError:
            return "Деление на ноль недопустимо"

a = Division()
print(a.divide(10, 0))
print(a.divide(10, 1))