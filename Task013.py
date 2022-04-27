#Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

str1 = input("Введите первую строку для проверки:")
str2 = input("Введите вторую строку для поиска в первой строке:")

print(f"Вторая строка входит в первую {str1.count(str2)} раз(а).")

def text_find(a,b):

#Function will find occurence of word in the text

    count = 0
    i = 0
    while i <= len(a):
        if b in a[i: i+len(b)]:
            count += 1
            i += len(b)
        else:
            i += 1
    return count

a = "a тесты тесты тессс тесты"
b = "тесты"

print(f"Count of first word in second phrase: {text_find(a,b)}")
print(f"Count of first word in second phrase: {text_find('аааааааааа','аа')}")