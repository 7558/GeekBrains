# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
# величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("thirdtask.txt", "r", encoding="utf-8") as user_txt:
    allsal = 0
    salary = []
    allpeople = []
    content = user_txt.read().split("\n")
    for i in content:
        i = i.split()
        if int(i[2]) < 20000:
            salary.append(i[0])
        allsal += int(i[2])
        allpeople.append(i[0])
print(f"У данных людей оклад меньше 20т. р.: {salary}.\nСредний оклад: {allsal / len(allpeople)}")