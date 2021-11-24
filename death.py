a = int(input("Введите число А ="))
b = int(input("Введите число Б ="))
v = int(input("Введите число В ="))

while a < b:
    print(a, " меньше ", b)
    a = a+v
if a==b:
    print(a, " равно ", b)
else:
    print(a, " больше ", b)
print("Цикл окончен")
