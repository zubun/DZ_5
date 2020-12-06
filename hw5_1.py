'''Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.'''

with open ("test_1.txt", "w") as text:
    line = input("Введите строку: \n")
    while line:
        print(line, file=text)
        line = input("Введите строку: \n")
        if not line:
            break

text = open ("test_1.txt", "r")
text_2 = text.read()
print(text_2)
text_2 = text.read()
