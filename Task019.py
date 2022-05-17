# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел.

"""import time

x = time.time()
timespot = str(x)
rand = ''
expo = int(input('Введите количество знаков в нужном Вам случайном числе: '))

print(x)
for i in range (-expo, 0):
    ran = ran + timespot[i]
print(rand)


import os
from time import time
os.system("cls")

print(time() % 10/10, '\n')"""

# Линейный конгруэнтный метод: x(n+1) = (a * x(n) + b) / m

m = 100
b = 3
a = 2
x =1
c = 10

list = []

for i in range (c):
    x = (a * x  + b) % m
    list.append(x)
print(list)

