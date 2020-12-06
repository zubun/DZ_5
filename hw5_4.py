'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''

russian_numerals = []
with open(r"test_4.txt", "r", encoding="utf-8") as file:
    for line in file:
        english_numerals = line.split()

        if english_numerals[0] == "One":
            english_numerals.pop(0)
            english_numerals.insert (0, 'Один')
            russian_numerals.append(' '.join(english_numerals))

        elif english_numerals[0] == "Two":
            english_numerals.pop(0)
            english_numerals.insert (0, 'Два')
            russian_numerals.append(' '.join(english_numerals))

        elif english_numerals[0] == "Three":
            english_numerals.pop(0)
            english_numerals.insert (0, 'Три')
            russian_numerals.append(' '.join(english_numerals))

        elif english_numerals[0] == "Four":
            english_numerals.pop(0)
            english_numerals.insert (0, 'Четыри')
            russian_numerals.append(' '.join(english_numerals))

    russian = ' \n'.join(russian_numerals)
    with open("test_4_1.txt", "w") as text:
        print(f"{russian}", file=text)