def add(x, y):
    return x+y
print(add(1,2))
print(add('I a', 'm tester'))
def arg (a,b,c=2,d=3):
    return a+b+c+d
print(arg(1,1,1,1))
print(arg(2,2))
# print(arg(2,2,'1',1))
def range_arc(a,b,c,d):
    return a+' '+b+' '+c+' '+d
print(range_arc('1', '2', '3', '4'))
print(range_arc('1', '2', d='3', c='4'))
def zadacha_1(a=(1,2,3,4)):
    return a[0]
print(zadacha_1((5,8,4,6)))
def zadacha_2(radius, pi=3.14159):
    return pi*radius**2
print(zadacha_2(5))
