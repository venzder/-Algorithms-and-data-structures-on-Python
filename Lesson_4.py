import random
import timeit

x = [random.randint(1, 99) for i in range(10)]
print(x)


def f(list_num):
    y = []
    for i, j in enumerate(list_num):
        if j % 2 == 0:
            y.append(i)
    return y


print(f(x))

TEST_CODE = '''
import random
list_num = [random.randint(1, 99) for i in range(10)]
f(list_num)
'''

t = timeit.timeit(stmt=TEST_CODE, setup="from __main__ import f", number=10000)

print(t)

# Сложность O(n)
# Время 0.157338832