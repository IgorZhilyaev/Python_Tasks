#Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

"""N = int(input('Введите число N:'))

elements = []
mult = 1

f = open('file.txt', 'r')

for i in range(-N, N + 1):
    elements.append(i)

print(elements)

for i in f:
    mult = mult * int(elements[int(i)])

print(mult)

f.close()"""

"""
n=int(input('Введите N (целое число), значение до которрого будет формироваться список: '))
pos=input(f'Введите, через запятую, позиции элементов которые необходимо перемножить, не более {n*2}: ').split(',')

with open('positions.txt', 'w') as positions:
    for i in pos:
        positions.write(f'{i}\n')

spisok=[]
step = 1
start = -n
stop = n+1
if n < 0:
    step = -1
    stop -= 2
for i in range(start, stop, step):
    spisok.append(i)

print(spisok)

multiply=1

with open('positions.txt', 'r') as positions:
    for element in positions:
        multiply*=spisok[int(element.strip())]

print(f'Произведение элементов с введенными позициями равно {multiply}')
"""

from functools import reduce
import os
import random
os.system("cls")

n = random.randint(16, 26)

list = [i for i in range(-n, n+1)]

print('Задан список: ', list, '\n')

with open('task017.txt', 'w') as data: # случайным образом задаем позиции и записываем в файл
    for i in range(int(n/2)):
        data.write(f'{random.randint(0, n*2)}\n')

def read2list(file): # читает в список из файла
    with open(file, 'r') as file:
        position_index = [int(line.strip()) for line in file.readlines()]
        position_index.sort()
        print('Выбраны позиции с индексами: \t', *position_index)
    return position_index


position_index = read2list('task017.txt')
position_element = [list[i] for i in position_index]
mult = reduce((lambda x, y: x*y), position_element)

print('Элементы на указанных позициях:\t', *position_element,
'\nИх произведение равно : \t', mult, '\n')
