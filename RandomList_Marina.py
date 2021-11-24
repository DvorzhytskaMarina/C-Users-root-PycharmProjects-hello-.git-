import random

list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
k = int(input("Введите необходимое количество элементов = "))
randList = random.sample(list, k)

print("Список случайных чисел из",k, "элементов", randList)
