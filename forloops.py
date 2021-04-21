# """
# #76
# n = int(input('enter n:'))
#
# while n > 0:
#     print("silence is gold")
#     n -= 1
#
# n = int(input('enter n:'))
# i = 0
#
# for i in range(n):
#     print("silence is golden")
#
# #77while
# n = int(input('enter n:'))
#
# while n > 0:
#     print("00000")
#     n -= 1
#
# #77for
# n = int(input('enter n:'))
#
# for i in range(n):
#     print("00000")
#
#
# #78
# n = int(input('enter n:'))
# i = 0
#
# while n > i:
#     print("*****")
#     n -= 1
#
#
# #78for
# n = int(input('enter n:'))
#
# for i in range(n):
#     print("*****")
#
#
# #79while
# i = 1
#
# while i <= 20:
#     print(i)
#     i += 1
#
# #79for
# i = 1
#
# for i in range(21):
#     print(i)
#
# #80while
# start = 1001
# end = 1025
#
# while start <= end:
#     print(start)
#     start += 4
#
# #80for
# for i in range(1001, 1025, 3):
#     print(i)
#
# #81while
# start = 100
# end = 0
#
# while start >= end:
#     print(start)
#     start -= 4
#
# #81for
# for i in range(100, 1, -4):
#     print(i)
#
#
# #82while
# start = 1.2
# end = 2.8
#
# while start <= end:
#     print(start)
#     start += 0.2
#
# #82for
#
# for i in range(1.2, 2.8, 0.2):
#     print(i)
#
# #83
# start = 25
# end = 35
#
# while start <= end:
#     print(start, start + .5, start - .2)
#     start += 1
#
# #84
# start = 1
# end = 100
#
# while start <= end:
#     print(start, start * 70, start * 3.5)
#     start += 1
#
# #84for
# for i in range(1, 101):
#     print(i, i * 70, i * 3.5)
#     i += 1
#
#
# #86while
# n = int(input('enter number'))
# i = 0
# result = 0
#
# while i <= n:
#     result += i
#     i += 1
# print(result)
#
#
# #86for
# n = int(input('enter number'))
# mysum = 0
#
# for i in range(n):
#     mysum += i
# print(mysum)
#
#
# #87while
# start = 10
# end = 88
# result = 0
#
# while start <= end:
#     result += start
#     start += 1
# print(result)
#
# #87for
# mysum = 0
# for i in range(10, 89):
#     mysum += i
# print(mysum)
#
#
# thislist = ["banana", "apple", "cherry", "mango", "kiwi"]
# thislist.insert(1, "mysum")
# print(thislist)
"""

fruits = ["apple", "banana", "kiwi", "orange", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


fruits = ["apple", "banana", "kiwi", "orange", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "kiwi", "orange", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "kiwi", "orange", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
"""
