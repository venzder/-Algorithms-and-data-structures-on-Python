# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.

import collections

count_enterprises = int(input("Введите количество предприятий: "))
Enterprise = collections.namedtuple('Enterprise', ['q1', 'q2', 'q3', 'q4', 'ear'])
enterprises = {}
profit = []
lager = []
less = []
i = 1
while i <= count_enterprises:
    name_enterprise = input("Введите название предприятия: ")
    a = int(input("Введите прибыль за первый квартал: "))
    b = int(input("Введите прибыль за второй квартал: "))
    c = int(input("Введите прибыль за третий квартал: "))
    d = int(input("Введите прибыль за четвертый квартал: "))
    e = a + b + c + d
    enterprises[name_enterprise] = Enterprise(q1=a, q2=b, q3=c, q4=d, ear=e)
    profit.append(e)
    i += 1
average = sum(profit)/count_enterprises
for key in enterprises:
    if average < enterprises[key].ear:
        lager.append(key)
    elif average > enterprises[key].ear:
        less.append(key)

print(f'Больше среднего прибыль у {lager}')
print(f'Меньше среднего прибыль у {less}')

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
# [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].