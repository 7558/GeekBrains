# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

userAnswer = input("Введите строку из нескольких слов разделенных пробелами: ")

userAnswer = userAnswer.split()

count = 1
for i in userAnswer:
    if len(i) < 10:
        print(f" {count} строка: {i}")
        count += 1
    else:
        print(f" {count} строка: {i[0:10]}")
        count += 1
