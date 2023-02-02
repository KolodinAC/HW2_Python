# Задача №4 HARD Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

try:
    n = int(input('Введите желаемую длину ряда Фибоначчи: '))

    int_array1 = [0, 1]
    fib1 = 0
    fib2 = 1
    i = 0
    while i < n - 1:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        int_array1.append(fib_sum)
        i = i + 1

    a = len(int_array1)
    int_array2 = [1] * a

    i = 0
    while i < len(int_array2):
        int_array2[i] = int_array1[i]
        i += 1

    el = 0
    while el < len(int_array2):
         int_array2[el] *= -1
         el += 1

    int_array2.remove(0)
    int_array2.reverse()
    int_array3 = int_array2 + int_array1

    print(int_array3)
except:
    print('Вы ввели неверные данные!')

