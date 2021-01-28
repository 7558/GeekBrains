# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

other_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четрые"}
recrt_dict = []
with open("fourthtask.txt", "r", encoding="utf-8") as content:
    for i in content:
        i = i.split(" ", 1)
        recrt_dict.append(other_dict[i[0]] + ' ' + i[1])

with open("newfourhttask.txt", "w", encoding="utf-8") as content:
    content.writelines(recrt_dict)

