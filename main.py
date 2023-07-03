x = input("Введите строку: ")

new_string = x.replace(" ", "-")

words = new_string.split("-")
print("Слова:")
for word in words:
    print(word)

character_x = 0
for char in x:
    character_x += 1

digit_x = 0
for char in x:
    if char.isdigit():
        digit_x += 1

number_x = 0
for word in x.split():
    if word.isdigit():
        number_x += 1

letter_x = 0
for char in x:
    if char.isalpha():
        letter_x += 1

uppercase_x = 0
for char in x:
    if char.isupper():
        uppercase_x += 1

lowercase_x = 0
for char in x:
    if char.islower():
        lowercase_x += 1

space_x = 0
for char in x:
    if char.isspace():
        space_x += 1

print("Количество символов:", character_x)
print("Количество цифр:", digit_x)
print("Количество чисел:", number_x)
print("Количество букв:", letter_x)
print("Количество букв в верхнем регистре:", uppercase_x)
print("Количество букв в нижнем регистре:", lowercase_x)
print("Количество пробелов:", space_x)

print("Обновленная строка:", new_string)

word_count = len(words)
print("Количество слов:", word_count)