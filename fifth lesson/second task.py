# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк,
# количества слов в каждой строке.

user_text = open("firsttask.txt", "r")
# content = user_text.read()
content = user_text.readlines()
print(f"Количество строк: {len(content)}")
for i in range(len(content)):
    print(f"Количество символов в {i+1} строке, {len(content[i])}")
user_text.seek(0)
content = user_text.read()
content = content.split()
print(f"Количество слов: {len(content)}")
user_text.close()