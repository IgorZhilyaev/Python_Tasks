# Показать первую цифру дробной части числа

n = float(input('Введите любое число с дробной частью: '))
d = int((n*10)%10)
print('Первая цифра дробной части: ', d)