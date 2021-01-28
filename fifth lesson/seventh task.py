# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
# средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

profit = {}
count = 0
prof = 0
profit_firm = {}
with open("seventhtask.txt", "r") as content:
    for i in content:
        name, form, earn, spend = i.split()
        profit[name] = int(earn) - int(spend)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            count += 1
    aver_profit = prof / count
    print(f"Средняя: {aver_profit}")
    profit_firm = {"Средняя": round(aver_profit)}
    profit.update(profit_firm)
    print(f"Прибыль компаний: {profit}")

with open("seventhtask.json", "w") as content:
    json.dump(profit, content)
    str = json.dumps(profit)
    print(f"Файл с json" + f" {str}")

