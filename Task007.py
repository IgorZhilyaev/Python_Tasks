# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = [True, False]
y = [True, False]
z = [True, False]

check = 1
for i in range (0, 2):
    for j in range (0, 2):
        for k in range (0, 2):
            if (not (x[i] or y[j] or z[k]) == (not x[i] and not y[j] and not z[k])):
                print(f'При х = {x[i]}, y = {y[j]}, z = {z[k]}  - выражение принимает значение "Истинно"')
            else:
                print(f'Выражение из условия - False')
                check = 0

if (check == 1):
    print('Выражение ИСТИННО!')
else:
    print('Выражение ЛОЖНО!')


"""def logic(x, y, z):
    if (not (x or y or z) == (not x and not y and not z)):
        result = True
    else:
        result = False
        print(result)
    return result

f1 = logic(True, True, True)
f2 = logic(True, True, False)
f3 = logic(True, False, True)
f4 = logic(False, True, True)
f5 = logic(True, False, False)
f6 = logic(False, False, True)
f7 = logic(False, True, True)
f8 = logic(False, False, False)

if (all([f1, f2, f3, f4, f5, f6, f7, f8])) == True:
    print('Выражение тождественно')
else:
    print('Выражение НЕ тождественно')"""

"""print('X Y Z F')
for x in a:
for y in a:
for z in a:
f = not(x or y or z) == (not x and not y and not z)
print (x, y, z, int(f))"""