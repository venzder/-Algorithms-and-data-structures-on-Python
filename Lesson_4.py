# import random
# import timeit
#
# x = [random.randint(1, 99) for i in range(10)]
# print(x)
#
#
# def f(list_num):
#     y = []
#     for i, j in enumerate(list_num):
#         if j % 2 == 0:
#             y.append(i)
#     return y
#
#
# print(f(x))
#
# TEST_CODE = '''
# import random
# list_num = [random.randint(1, 99) for i in range(10)]
# f(list_num)
# '''
#
# t = timeit.timeit(stmt=TEST_CODE, setup="from __main__ import f", number=10000)
#
# print(t)

# Сложность O(n)
# Время 0.157338832

# Задача 2
# без решета Эратосфена

import timeit

def simple_nums(n):
    lst = []
    k = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return lst

TEST_CODE = '''
n = 13
simple_nums(n)
'''

t1 = timeit.timeit(stmt=TEST_CODE, setup="from __main__ import simple_nums", number=10000)
print(t1)
# с решетом Эратосфена


def simple_nums_erat(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    return a


TEST_CODE_ER = '''
n = 13
simple_nums_erat(n)
'''

t2 = timeit.timeit(stmt=TEST_CODE_ER, setup="from __main__ import simple_nums_erat", number=10000)
print(t2)

print(simple_nums_erat(13))