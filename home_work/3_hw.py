# Задача 1
a=43
b=43
print("Задача 1")
if a>=b:
    print(a)
else:
    print(b)
# Задача 2
c=5
d=140
print('''
Задача 2''')
if c-d==135 or d-c==135:
    print('yes')
else:
    print('no')
# Задача 3
e=int(6)
print('''
Задача 3''')
if e==1 or e==2 or e==12:
    print('Зима')
elif 6>e>2:
    print('Весна')
elif 9>e>5:
    print('Лето')
elif 12>e>8:
    print('Осень')
else:
    print('Не является номером месяца')
# Задача 4
f=65
g=44
h=20
print('''
Задача 4''')
if f>10 and g>10 and h>10:
    print('yes')
else:
    print('no')
# Доп. задача 1
def function_1(i, j, k, l, m, summa=0):
    if i>0:
        summa+=1
    if j>0:
        summa+=1
    if k>0:
        summa+=1
    if l>0:
        summa+=1
    if m>0:
        summa+=1
    return summa
print ('''
Доп. задача 1''')
print(function_1(8, 23, -5, 56, -836))
# Доп. задача 2
def function_2 (years, months):
    months+=years*12
    days=months*29
    return days
print('''
Доп. задача 2''')
print(function_2(1, 1))