#dz4
#1
# Запускаю с параметрами python dz4.py 20 2500 4500

from sys import argv
path, time, stav, prem = argv
time, stav, prem = map(int, argv[1:])
res = time * stav + prem
print(f'заработная плата {res}')

#2
a = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [j for i, j in zip(a, a[1:]) if j > i]
print(new_list)

#3
my_list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(my_list)

#4
##[23, 1, 3, 10, 4, 11]
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in my_list if my_list.count(i) <= 1]
print(new_list)

#5
from functools import reduce
new = [i for i in range(100, 1001) if i % 2 == 0]
print(reduce(lambda x, y: x + y, new))

#6
from itertools import count, cycle
for el in count(-5):
    print(el)
    if el > 4:
        break

li = [10, 11, 12, 13, 14, 15]
new = []
i = 0
for el in cycle(li):
    new.append(el)
    i += 1
    if li == new:
        break
print(new)

#7
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr = pr * i
        yield pr
for i in fact(5):
    print(i)