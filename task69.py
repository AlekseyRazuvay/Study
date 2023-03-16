sum = 0

line = input("Введите возраст участника группы")

while line != "":
    age = int(line)
    if age < 2:
        sum = sum + 0
    elif age >= 2 or age <= 12:
        sum = sum + 14
    elif 12 < age < 65:
        sum = sum + 23
    elif age >= 65:
        sum = sum + 18
    line = input("Введите возраст участника группы")
else:
    print("Total = ", sum)
