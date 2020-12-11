'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
 их окладов (не менее 10 строк).
 Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
 Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''
underpaid = []
underpaid_list = ()
average_list = []
with open(r"test_3.txt", "r", encoding="utf-8") as file:
    for line in file:
        list = line.split()
        # list_2 = float(list[1])
        if float(list[1]) < 20000:
            underpaid.append(list[0])
            underpaid_list = ', '.join(underpaid)
        average_list.append(float(list[1]))
    average = sum(average_list) / len(average_list)

print(f'Сотрудники получающие заработную плату меньше 20 000 руб:\n{underpaid_list}.\nCредняя величина дохода сотрудников: {average:.2f} руб.')