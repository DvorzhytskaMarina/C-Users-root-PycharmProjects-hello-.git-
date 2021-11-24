a = int(input("Введите число = "))
x = a
y = 0

while x != 0:
    y = y + x % 10
    print(x % 10)
    x = int(x / 10)
    #print(x)
else:
    print("Сумма = ", y)

