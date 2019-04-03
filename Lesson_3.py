# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# a = [0]*8
# for i in range(2, 100):
#     for j in range(2, 10):
#         if i%j == 0:
#             a[j-2] += 1
# i = 0
# while i < len(a):
#     print(i + 2, ' - ', a[i])
#     i += 1

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
#
# import random
#
# x = [random.randint(1, 99) for i in range(10)]
# print(x)
# y = []
# for i, j in enumerate(x):
#     if j % 2 == 0:
#         y.append(i)
# print(y)


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# import random
#
# x = [random.randint(1, 99) for i in range(10)]
# print(x)
# print(max(x))
# print(min(x))
# a = x.index(min(x))
# b = x.index(max(x))
# x[a], x[b] = x[b], x[a]
# print(x)

# 4. Определить, какое число в массиве встречается чаще всего.

# import random
#
# x = [random.randint(1, 10) for i in range(100)]
# counts = []
# for i in x:
#     count = 0
#     for j in x:
#         if i == j:
#             count += 1
#     counts.append((i, count))
# counts = set(counts)
# count_max = []
# for i in counts:
#     count_max.append(i[1])
# maxim = max(count_max)
# if maxim <= 1:
#     print('Все значения уникальны')
# else:
#     for i in counts:
#         if i[1] == maxim:
#             print(f'Число {i[0]} встречается максимальные {i[1]} раз')

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

# import random
#
# x = [random.randint(-100, 100) for i in range(100)]
# minim = min(x)
# index = x.index(minim)
# print(f'Минимальное число {minim} с индексом {index}')

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

import random

x = [random.randint(1, 100) for i in range(50)]
sum_list = []
x_max = max(x)
x_min = min(x)
idx_min = x.index(x_min)
idx_max = x.index(x_max)
for idx, itm in enumerate(x):
    if idx_min < idx_max:
        if idx_max > idx > idx_min:
            sum_list.append(itm)
    elif idx_min > idx_max:
        if idx_max < idx < idx_min:
            sum_list.append(itm)
summa = sum(sum_list)
print(summa)

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
# являться минимальными), так и различаться.
# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.