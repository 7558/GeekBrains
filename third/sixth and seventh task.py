# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().
count = 1
def int_func(text):
    """Получаем слова через пробел, выводим каждое слово с большой буквы."""
    text = text.split()
    words = []
    global count
    for i in range(len(text)):
        formatText = text[i].capitalize()
        if count == 1:
            print(formatText)
            words.append(formatText)
    if count == 1:
        print(words)
        input("\n\nНажмите Enter, чтобы перейти ко второй функции.\n")
    return formatText


def int_func2(num):
    """Получаем слова на входе, с помощью функции int_func переводим первый символ в верхний регистр
    и склеиваем."""
    print("Работа второй функции функции.")
    global count
    count = 0
    num = num.split()
    proposal = ""
    for i in range(len(num)):
        formatText = str(int_func(num[i]))
        proposal += formatText + " "
    print(proposal)




text = input("Введите слова, у которых нужно преобразовать первый символ в верхний: ")

int_func(text)

int_func2(text)