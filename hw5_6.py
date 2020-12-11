'''Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и
лабораторных занятий по этому предмету и их количество. Важно,
 чтобы для каждого предмета не обязательно были все типы занятий.
 Сформировать словарь, содержащий название предмета и общее
 количество занятий по нему. Вывести словарь на экран.
Примеры строк файла: Информатика:       100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
def adding_to_the_dist(el):
    key = el[0]
    number_of_classes = []
    for i in el:
        if i.endswith('(л)'):
            number = int((i.replace('(л)','')))
            number_of_classes.append(number)
        elif i.endswith('(пр)'):
            number = int((i.replace('(пр)','')))
            number_of_classes.append(number)
        elif i.endswith('(лаб)'):
            number = int((i.replace('(лаб)','')))
            number_of_classes.append(number)
    summa = sum(number_of_classes)
    dist = { key[0:-1]: sum(number_of_classes)}
    return dist



f = open ("test_6.txt", "r", encoding="utf-8")
file = f.readlines()
result = {}
for el in range(len(file)):
    line = file[el].split()
    result.update(adding_to_the_dist(line))

print(result)
f.close()


# print(file)
# a = file[0].split()
# print(type(a))
# cv = adding_to_the_dist(a)
# print(cv)
# b = a[2]
# print(b.endswith('(пр)'))
# print(type(int(b.replace('(пр)',''))))

# for el in b:
#     print(ord(el))
# print(a)
# print(b)
# print(list(print(file_1) for el in file_1))
