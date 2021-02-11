# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран./

with open("fifthtask.txt", "w+", encoding="utf-8") as content:
    user_answer = input("Введите цифры через пробел: ")
    content.writelines(user_answer)
    numbers = user_answer.split()
    count = 0
    for i in numbers:
        i = int(i)
        count += i
    print(f"Общая сумма: {count}")
