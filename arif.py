a = int(input("Введите число А ="))
b = int(input("Введите число В ="))

print("Сумма = ", a+b)
print("Разность = ", a-b)
print("Произведение = ", a*b)
if b==0 :
    print("invalid input!!!")
else: print("Частное = ", round(a/b, 2))