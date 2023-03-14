from math import sqrt

perimetr = 0

print("Введите координаты x и y")

x = float(input("Введите x: "))
y = float(input("Введите y: "))

first_x = x
first_y = y

line = input("Введите следующую координату X : ")

while line != "":
        second_x = float(line)
        second_y = float(input("Введите следующую координату y = "))
        dist = sqrt((first_x - second_x) ** 2 + (first_y - second_y) ** 2)
        perimetr = perimetr + dist

        first_x = second_x
        first_y = second_y

        line = input("Введите следующую координату X : ")

else:
    dist = sqrt((x - second_x) ** 2 + (y - second_y) ** 2)
    perimetr = perimetr + dist
    print("Периметр = ", perimetr)




