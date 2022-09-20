## dz3
# 1
def my_numbers():
    try:
        num1 = int(input('введите первое число: '))
        num2 = int(input('введите второе число: '))
        d = num1 / num2
        print(d)
    except:
        print('На ноль делить нельзя, введите целое число')
my_numbers()

# 2
def people(name, surname, year, city, email, tel_num):
    print(f"Имя = {name}, Фамилия = {surname}, Год = {year}, Город = {city}, Эл.почта = {email}, Тел.номер = {tel_num}")
people('Иван', 'Петров', '1965', 'Москва', 'ivan@mail.ml', '89073451298')
people(name = input('Введите имя: '), surname = input('Введите фамилию: '), year = input('Введите год: '), city = input('Введите город: '), email = input('Введите email: '), tel_num = input('Введите телефонны номер: '))

# 3
def my_func(a, b, c):
    if a >= b and c >= b:
        return a + c
    elif b > a and c > a:
        return b + c
    elif b > c and a > c:
        return a + b

sum = my_func(a = int(input("enter a: ")), b = int(input("enter b: ")), c = int(input("enter c: ")))
print(sum)

# 4
def my_func(x, y):
    a = (x**y)
    print(a)
my_func(31, -2)

def my_func(x, y):
    a = 1
    for i in range(abs(y)):
        a *= x
    if y >= 0:
        return a
    else:
        return 1 / a
print(my_func(31, -2))

# 5
def my_num():
    res1 = 0
    while True:
        number = input('Введите числа или stop для завершения: ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'stop':
                return
            else:
                res = res + int(number[el])
        res1 = res1 + res
        print(res1)
my_num()

#6
def my_func(text):
	return text.title()
print(my_func("этот текст"))

# 7
def int_func():
    text = input("enter: ")
    print(text.title())
int_func()

