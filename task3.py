# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = 333
list = list(filter(lambda x: N % x == 0, [i for i in range(1, N + 1)]))  #filter, lambda, list comprehension
print(list)