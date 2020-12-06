'''Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.'''

count_line = 0
count_word = 0
count_word_all = 0
symbol = 0
symbol_all = 0
with open(r"test_2.txt", "r") as file:
    for line in file:
        count_line += 1
        count_word = len(line.split())
        count_word_all += count_word
        symbol = len(line)
        symbol_all += symbol
        print(f"Строка: {count_line} - количество слов: {count_word}, кол-во символов {symbol}.")
print(f"Итого:\nОбщее ко-во строк: {count_line}\nОбщее кол-во слов: {count_word_all}\nОбщее кол-во символов: {symbol_all}")