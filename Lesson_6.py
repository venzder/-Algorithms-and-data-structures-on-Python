# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Python 3.7.3, ОС 64 разрядная
# Размер переменной x равен 268
# Размер переменной x_max равен 14
# Размер переменной x_min равен 14
# Размер переменной idx_min равен 14
# Размер переменной idx_max равен 14
# Размер переменной sum_list равен 136
# Размер переменной summa равен 14

import random
import sys

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
print(x)
print(f'Размер переменной x равен {sys.getsizeof(x)}')
print(f'Размер переменной x_max равен {sys.getsizeof(x_max)}')
print(f'Размер переменной x_min равен {sys.getsizeof(x_min)}')
print(f'Размер переменной idx_min равен {sys.getsizeof(idx_min)}')
print(f'Размер переменной idx_max равен {sys.getsizeof(idx_max)}')
print(f'Размер переменной sum_list равен {sys.getsizeof(sum_list)}')
print(f'Размер переменной summa равен {sys.getsizeof(summa)}')