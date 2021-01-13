# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
# git.

userInput = input("Введите число, которое необходимо суммировать: ")

valueFirst = int(userInput*2)
valueSecond = int(userInput*3)

result = int(userInput) + valueFirst + valueSecond

print("Считаем " + userInput + " + " + str(valueFirst) + " + " + str(valueSecond) + " = " + str(result))

