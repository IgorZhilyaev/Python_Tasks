# Найти максимальное из пяти чисел

from ast import For


massive = [4, 12, 7, 8, 14]

print('\n', massive)
print('Наибольшее число: ', max(massive)) # первый способ

max = massive[0]
for i in massive:
    if i>max:
        max = i
print('Наибольшее число: ', max, '\n') # второй способ

a, b, c, d, e = 3, 5, 7, 2, 3

max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
if max < e:
    max = e
print('Наибольшее число: ', max, '\n') # третий способ