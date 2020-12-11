'''Создать (программно) текстовый файл, записать в него программно
набор чисел,разделенных пробелами. Программа должна подсчитывать сумму чисел
в файле и выводить ее на экран.
'''
from random import randint

with open("test_5.txt", "w+") as f:
    list = list([randint(0,100) for el in range(30)])
    # list = list((el ** 5 - el for el in range(5,20)))
    # list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
    # print(list)
    print(f'Сумма чисел в файле ровняется {sum(list)}!!!')
    list_1 = []
    list_1 = ' '.join(map(str, list))
    print(f"{list_1}", file = f)

# f = open ("test_5.txt", "r")
# file_1 = f.read()
# print(file_1)
# f.close()


