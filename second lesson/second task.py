#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

listRandom = list(input("Введите желаемые элементы: "))

print(listRandom)
print(len(listRandom))

begin = 0
for i in range(int(len(listRandom)/2)):
    listRandom[begin], listRandom[begin + 1] = listRandom[begin + 1], listRandom[begin]
    begin += 2

print(listRandom)
