##dz5

#1
f = open(r'file.txt', 'w', encoding='utf-8')
new = input('введите текст через пробел: ').split()
for i in new:
    f.write(i + '\n')
f.close()

#2
f = open(r'file2.txt', 'w', encoding='utf-8')
l = 0
s = 0
w = 0
new = ["first car", "second hello world", "third blue bird"]
for i in new:
    f.write(i + '\n')
    s += len(i.replace(' ', ''))
    l += 1
    w += len(i.split())
    print(i)
print('всего символов:', s)
print('всего строк:', l)
print('всего слов:', w)
f.close()

# 3
with open(r'file3.txt', 'r', encoding='utf-8') as f:
    o = []
    p = []
    mylist = f.read().splitlines()
    for i in mylist:
        i = i.split()
        if float(i[1]) < 20000:
            p.append(i[0])
        o.append(i[1])
    summa = sum(map(float, o)) / len(o)
    print(p)
    print('%.2f' % summa)

#4
with open(r'file4.txt', 'r', encoding='utf-8') as f:
    mylist = f.read()
list_en = ['One', 'Two', 'Three', 'Four']
list_ru = ['Один', 'Два', 'Три', 'Четыре']
for index, word in enumerate(list_en):
    if word in mylist:
        mylist = mylist.replace(word, list_ru[index])
with open(r'file4-1.txt', 'w', encoding='utf-8') as f:
    f.write(mylist)

#5
with open(r'file5.txt', 'w', encoding='utf-8') as f:
    num = []
    new = input('введите числа через пробел: ').split()
    for li in new:
        f.writelines(li + '\n')
        num.append(int(li))
    print(sum(num))
