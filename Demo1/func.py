# # from math import *
# #
# #
# # def quadratic(a, b, c):
# #     x1 = (-b+sqrt(pow(b, 2)-4*a*c))/(2*a)
# #     x2 = (-b-sqrt(pow(b, 2)-4*a*c))/(2*a)
# #     return x1, x2
# #
# #
# # # 测试:
# # print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# #
# # print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
# #
# # if quadratic(2, 3, 1) != (-0.5, -1.0):
# #     print('测试失败')
# # elif quadratic(1, 3, -4) != (1.0, -4.0):
# #     print('测试失败')
# # else:
# #     print('测试成功')
#
#
# def product(*args):
#     if len(args) == 0:
#         raise TypeError
#     else:
#         i = 1
#         for y in args:
#             i = y*i
#         return i
#
#
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')
#
#
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(950))


# def fact(n):
#     return fact_iter(n, 1)
#
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
#
#
# print(fact(1000))

# def move(n, a, b, c):
#     if n == 1:
#         print(a, '-->', c)
#     else:
#         move(n-1,a,c,b)
#         move(1,a,b,c)
#         move(n-1,b,a,c)
#
#
# # 期待输出:
# # A --> C
# # A --> B
# # C --> B
# # A --> C
# # B --> A
# # B --> C
# # A --> C
# move(4, 'A', 'B', 'C')


# def trim(s):
#     if len(s) == 0:
#         return s
#     elif s[-1] == ' ':
#         return trim(s[:-1])
#     elif s[0:1] == ' ':
#         return trim(s[1:])
#     else:
#         return s
#
#
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

