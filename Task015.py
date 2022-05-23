#Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

import os
import math
from itertools import accumulate
import operator
os.system("cls")

n = int(input('Введите число N: '))

print(' Задать последовательность из', n, 'элементов\n',
'Последовательность:', *list(accumulate([x for x in range(1, n + 1)], operator.mul)), '\n')

"""
list = [1]

for i in range(2, n+1):
    list.append(i * list[i-2])

print('\n',list, '\n')

def multy(a):
    if a == 1:
        return 1
    return a * multy(a-1)

# n = 5

print("Sequence for ")
for i in range(1, n+1):
    print(multy(i), end=' ')

print("\nФакториал: ")
a = math.factorial(5)
print(a)
"""