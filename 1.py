# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# старый вариант 

float_num = input('input float number: ')
print(type(float_num))
sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)
print(sum)

# Новый 

a = float(input('Введите число: '))
new_sum = sum(map(int, str(a).replace('.', '')))
print(new_sum)

# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# старый вариант 

n = int(input('input N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
    print(factorial, end=' ')

# Новый вариант

from math import factorial

n = int(input('Введите число: '))
f = lambda x: 1 if x == 0 else x * factorial(x - 1)
list2 = list( f(i) for i in range(1, n +1))
print(list2)

#  Задача 3 Реализуйте алгоритм перемешивания списка.
# старый вариант решений

from random import Random, randint

N = int(input('Введите число '))
numbers = []
for i in range(N):
    numbers.append(randint(-N,N+1))
print(numbers)

def smes(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(smes(numbers))

# новый вариант решений

import random
my_list = [random.randint(1,10) for i in range(random.randint(3,8))]
print(f"Наш список: {my_list}")
random.shuffle(my_list)
print(f"Наш список после перемешивания: {my_list}")

# Задача 4. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности
# старый вариант

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")

# новый вариант

l = [1, 2, 3, 4, 4, 3, 8, 9, 1]
result_list = list(filter(lambda a: l.count(a) == 1, l))
print(result_list)
