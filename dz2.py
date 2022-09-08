# 1
li = [12, 'Bob', 466, 48.2, 'Jon', 12.23, True, 45.6]
for i in li:
    print(type(i), i)

# 2
li = input("Введите элементы списка: ").split()
li[:-1:2], li[1::2] = li[1::2], li[:-1:2]
print(li)

# 3
mes = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
m = int(input('Введите месяц: '))
for el in mes:
    if m in mes[el]:
        print(el)
        break

mes = ['Зима', 'Весна', 'Лето', 'Осень']
m = int(input('Введите месяц: '))
if m ==12 or m ==1 or m==2:
    print(mes[0])
if m ==3 or m ==4 or m==5:
    print(mes[1])
if m ==6 or m ==7 or m==8:
    print(mes[2])
if m ==9 or m ==10 or m ==11:
    print(mes[3])


# 4
st = input('введите: ').split()
for i, el in enumerate(st, 1):
    print(f'{i}, {el[:10]}')

#5
items = [7, 5, 3, 3, 2]
print(f"Рейтинг - {items}")
m = int(input('Введите число: '))
for i in range(len(items)):
    if items[i] == m:
        items.insert(i + 1, m)
        break
    elif items[0] < m:
        items.insert(0, m)
    elif items[-1] > m:
        items.append(m)
print(f"Рейтинг - {items}")


