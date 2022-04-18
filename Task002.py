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


