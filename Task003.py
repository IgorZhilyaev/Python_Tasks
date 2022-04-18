# Вывести на экран числа от -N до N

from operator import and_


num = int(input('Введите число: '))
for i in range (-num, num + 1):
    print(i, end=' ')
