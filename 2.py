string = input("Введите строку: ")
length = len(string)

for index, char in enumerate(string):
    if index == 2:
        continue

    if char == "c":
        print("В строке есть символ 'c'")
    s = string[:2] + string[3:]

print("Длина строки:", length)
print("Строка без третьего символа и без последнего символа:", s[:-1])
