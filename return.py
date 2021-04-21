# 34
# a = int(input('enter number'))
#
# if a > 3:
#     print(a * 10)
# else:
#     print(a / 10)
#
# #35
# n = int(input('enter number'))
#
# if n < 7:
#     print('yes')
# elif n > 10:
#     print("no")
# elif n == 9:
#     print("error")
#
# #36
# n = int(input("enter month: "))
#
# if n == 1:
#     print("january")
# elif n == 2:
#     print("february")
# elif n == 3:
#     print("march")
# elif n == 4:
#     print("april")
# elif n == 5:
#     print("may")
# elif n == 6:
#     print("june")
# elif n == 7:
#     print("july")
# elif n == 8:
#     print("august")
# elif n == 9:
#     print("september")
# elif n == 10:
#     print("october")
# elif n == 11:
#     print("novermber")
# elif n == 12:
#     print("december")
# else:
#     print("error")
#
#
# #37
# a = int(input('enter a:'))
# b = int(input('enter b:'))
#
# if a > b:
#     print("a is higher")
# elif b > a:
#     print("b is higher")
# else:
#     print("equal")
#
#
# #38
# a = int(input('enter a:'))
# b = int(input('enter b:'))
#
# if a * 10 > (b * 10) or b * 10 > a * 10:
#     print("yes")
# else:
#     print("no")
#
#
# #39
# a = int(input('enter a: '))
# b = int(input('enter b: '))
#
# if a > b:
#     print("yes")
# else:
#     print("a: " + str(b) + " b: " + "a")
#
#
# #40
# n = int(input("enter n: "))
#
# if -10 < n < 10:
#     print(n * 5)
# else:
#     print(n / 10)
#
# #41
# n = int(input('enter n: '))
#
# if 100 < n < -100:
#     print(0)
# else:
#     print(n * 10)
#
# #42
# n = int(input('enter n: '))
#
# if 2 < n < 5:
#     print(n * 10)
# elif 7 < n < 40:
#     print(n / 100)
# elif n > 300 or n < 0:
#     print(n * 3)
# else:
#     print(0)
#
# #43
# n = int(input('enter n: '))
#
# if n == 12 or n < 3:
#     print("winter")
# elif n >= 3:
#     print("spring")
#
#
# #44
# a = int(input('enter a: '))
# b = int(input('enter b: '))
#
# if a == 10 and b == 10 and a % 2 == 0:
#     print(a + b)
# else:
#     print(a * b)
#
#
# #45
# a = int(input('enter a: '))
# b = int(input('enter a: '))
# c = int(input('enter a: '))
#
# if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
#     print("yes")
# else:
#     print("no")
#
#
# #46
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
#
# if a % 5 == 0 and b % 5 == 0 and c % 5 == 0:
#     print(a + b + c)
# elif a % 5 == 0 and b % 5 == 0 and c % 5 != 0:
#     print(a + b)
# elif a % 5 == 0 and b % 5 != 0 and c % b == 0:
#     print(a + c)
# elif a % 5 != 0 and b % 5 == 0 and c % 5 == 0:
#     print(b + c)
# else:
#     print("error")
#
# #47
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
#
# if a > b and a > c:
#     print('a is higher')
# elif b > a and b > c:
#     print("b is higher")
# elif c > a and c > b:
#     print('c is higher')


# 48
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
#
# if a > c and b > c:
#     print(a + b)
# elif a > b and c > b:
#     print(a + c)
# elif b > a and c > a:
#     print(b + c)
# else:
#     print("error")

# 49
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
# d = int(input('enter d: '))
#
# if a > b and a > c and a > d and a % 2 == 0:
#     print("a: " + str(a))
# elif b > a and b > c and b > d and b % 2 == 0:
#     print("b: " + str(b))
# elif c > a and c > b and c > d and c % 2 == 0:
#     print("c: " + str(c))
# elif d > a and d > b and d > c and d % 2 == 0:
#     print("d: " + str(d))
# else:
#     print("error")


# #50
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
#
# if a == b and b == c or a == b and a != c or a == c and  c != b or b == c and b != a:
#     print("yes")
# else:
#     print("no")


# #51
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
#
# if a + b == c:
#     print("yes")
# elif a + c == b:
#     print("yes")
# elif b + c == a:
#     print("yes")
# else:
#     print("no")


# 52
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
# d = int(input('enter d: '))
#
# if a > 5 and b > 5 and c % 6 == 0 and d % 4 != 0:
#     print("yes")
# else:
#     print("no")


# 53
# a = int(input('enter a: '))
# b = int(input('enter b: '))
#
# if a > 30 or b > 30:
#     print("yes")
# else:
#     print("no")

# 54

# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
#
# if a > 30 and b > 30 and c < 30:
#     print("yes")
# elif a > 30 and b < 30 and c > 30:
#     print("yes")
# elif a < 30 and b > 30 and c > 30:
#     print("yes")
# else:
#     print("no")

# #55
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
#
# if a > 0 and b > 0 and c > 0:
#     print("total: " + str(3))
# elif a > 0 and b > 0 and c < 0 or a > 0 and b < 0 and c > 0 or a < 0 and b > 0 and c > 0:
#     print("total: " + str(2))
# elif a > 0 and b < 0 and c < 0 or a < 0 and b > 0 and c < 0 or a < 0 and b < 0 and c < 0:
#     print("total: " + str(1))
# else:
#     print("error")
#
# #57
# a = int(input('enter a: '))
# b = int(input('enter b: '))
# c = int(input('enter c: '))
#
# if 12 >= a > 0 and 31 >= b > 0 and 1990 < c < 2022:
#     print("yes")
# elif a == 2 and b == 28 and 1990 < c < 2022:
#     print("yes")
# elif a == 4 or a == 6 or a == 9 or a == 11 and b == 31:
#     print("no")
# else:
#     print("no")

#
# #forloops
# #75
# for i in range(10):
#     print('you are welcome')

# n = 10
# while n > 0:
#     print('you are welcome')
#     n -= 1


# #76
# n = int(input('enter n: '))
# for i in range(n):
#     print('silence is golden')

# n = int(input('enter n:'))
# while n > 0:
#     print("silence is golden")
#     n -= 1

# #77
# n = int(input('enter n: '))
# for i in range(n):
#     print("*****")

# n = int(input('enter n:'))
#
# while n > 0:
#     print("*****")
#     n -= 1

# #79
#
# i = 1
#
# while i <= 20:
#     print(i)
#     i += 1
#
# for i in range(21):
#     print(i)

# #80
# i = 1001
#
# while i <= 2025:
#     print(i)
#     i += 3
#
# for i in range(1001, 1025, 3):
#     print(i)

# #81
# start = 100
#
# while start >= 0:
#     print(start)
#     start -= 4
#
# for i in range(100, 0, -4):
#     print(i)

#
# #82
# start = 1.2
# end = 2.8
#
# while start <= end:
#     print(start)
#     start += 0.2

# #83
# start = 25
# end = 35
#
# while start <= end:
#     print(start, start + .5, start - .2)
#     start += 1

# ARRAYS_____________________________

# #1
# x = []
# i = 0
# n = 10
#
# while i < n:
#     if i == 0 or i == 9:
#         x.append(1)
#     else:
#         x.append(0)
#     i += 1
#
# print(x)

# #2
# x = []
# i = 0
# n = 10
#
# while i < n:
#     if i % 2 == 0:
#         x.append(0)
#     else:
#         x.append(1)
#     i += 1
#
# print(x)

# #3
# x = []
# i = 0
# n = 10
#
# while i < n:
#     if i % 2 == 1:
#         x.append(i)
#     i += 1
#
# print(x)

# 5
# x = []
# i = 0
# n = 10
#
# while i < n:
#     if i % 2 == 0:
#         x.append(i)
#     i += 1
#
# # print(x)
#
# x = []
# i = 59
#
# while i > 0:
#     if i % 3 == 0:
#         x.append(i)
#     i -= 1
#
# print(x)
#
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# n = int(input('enter n: '))
#
# print(n in x)



