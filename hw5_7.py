'''Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import json
def adding_dist(el):
    key = el[0]
    number_of_classes = int(el[2]) - int(el[3])
    # for i in el:
    #     if i.endswith('(л)'):
    #         number = int((i.replace('(л)','')))
    #         number_of_classes.append(number)
    #     elif i.endswith('(пр)'):
    #         number = int((i.replace('(пр)','')))
    #         number_of_classes.append(number)
    #     elif i.endswith('(лаб)'):
    #         number = int((i.replace('(лаб)','')))
    #         number_of_classes.append(number)
    # summa = sum(number_of_classes)
    dist = { key: number_of_classes}
    return dist



f = open ("test_7.txt", "r", encoding="utf-8")
file = f.readlines()
result = {}
outcome = []
for el in range(len(file)):
    line = file[el].split()
    result.update(adding_dist(line))
# print(result)
outcome.append(result)
profit = []
for el in result.values():
    if el > 0:
        profit.append(el)
average_profit = sum(profit) / len(profit)
outcome.append({'average_profit': average_profit})

with open("my_file.json", "w", encoding="utf-8") as write_f:
    json.dump(outcome, write_f)

print(outcome)
f.close()