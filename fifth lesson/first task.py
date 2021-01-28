# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка./

with open("firsttask.txt", "a") as user_input:
    user_Answer = 0
    while user_Answer != "":
        user_Answer = input("Что необходимо добавить? Выход - Enter: ")
        user_input.write(user_Answer + "\n")



user_text = open("firsttask.txt", "r")
content = user_text.read()
print(content)
user_text.close()

