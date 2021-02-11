# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

userAnswer = int(input("Ведите цифру месяца: "))

season_list = ["зима из списка", "весна из списка", "лето из списка", "осень из списка"]
season_dict = {1: "зима из словаря", 2: "весна из словаря", 3: "лето из словаря", 4: "осень из словаря"}

if userAnswer == 1 or userAnswer == 2 or userAnswer == 12:
    print(season_dict[1])
    print(season_list[0])
elif userAnswer == 3 or userAnswer == 4 or userAnswer == 5:
    print(season_dict[2])
    print(season_list[1])
elif userAnswer == 6 or userAnswer == 7 or userAnswer == 8:
    print(season_dict[3])
    print(season_list[2])
elif userAnswer == 9 or userAnswer == 10 or userAnswer == 11:
    print(season_dict[4])
    print(season_list[3])
else:
    print("Некорректный ввод")