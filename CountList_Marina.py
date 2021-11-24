import random

list1 = list(range(0, 10))
print(list1)

k = int(input("Введите необходимое количество элементов = "))
randList = random.sample(list1, k)

print("Список случайных чисел из",k, "элементов", randList)

y = int(input("Какое число найти для Вас? "))
n = randList.index(y)

print("Число", y, "находится в списке под номером", n)

