#dz4
#1
# Запускаю с параметрами python dz4.py 4 10 2

from sys import argv
path, ar1, ar2, ar3 = argv
p1, p2, p3 = map(int, argv[1:])
res = (p1 * p2) + p3
print(res)

#2