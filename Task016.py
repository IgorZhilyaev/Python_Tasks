# Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму.

import os
os.system("cls")

n = int(input('Введите число N: '))

#massive = []

#for i in range(1, n+1):
#    massive.append(1+(1/i)**i)
#print(f'Полученный массив:\n{massive}\n')
#print(f'Сумма чисел массива:\n{sum(massive):.2f}')

num = [1+(1/i)**i for i in range(1, n+1)]
print('Задана последовательность из ', n,
'чисел:\n', *num, '\nСумма чисел = ', round(sum(num), 2), '\n')