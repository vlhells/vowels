vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
aboba = input("Введите строку на латинице (английский алфавит):\n")
aboba = aboba.lower()
letters = len(aboba)
vowels = 0

for each in aboba:
    if each in vowels_list:
        vowels += 1

vowels_percent = (vowels / letters) * 100
print("Процент гласных в введённой строке (считается от всех символов, в т. ч. пробелы)):\n", vowels_percent, '%')
