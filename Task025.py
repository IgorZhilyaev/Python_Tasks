# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#   45 -> 101101
#   3 -> 11
#	2 -> 10

import os
from random import *
os.system("cls")

n = randint(1, 101)
print('Задано число: ', n, '\n')

print('Двоичный вид: ', "{0:b}".format(n))
print('Двоичный вид: ', bin(n)[2:])
