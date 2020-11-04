
import time


print("hello你好")
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print(counter)
print('hello, world')


a=1024*768

print("1024 * 768="+str(a))

print(10_000_000_000)
print('''line1
... line2
... line3''')

print(r'''hello,\n
world''')

print('''line1
line2
line3''')


x = b'ABC'
print(x)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

age=17
if age>=18:
    print(age)
    print("adult")
elif age<18:
    print("child")

print(list(range(5)))

d= {'a':1,'b':2,'a':3}

print(d.get('a', -1))


a = 'abc'
a=a.replace('a', 'A')
print(a)

help(abs)

print(str(1.23))
print(bool(0))