# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
listik = sum([i for num, i in enumerate([2, 4, 6, 7, 8, 5, 3]) if num % 2 != 0]) # enumerate, list comprehension
print(listik)