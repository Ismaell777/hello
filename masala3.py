# ZIP FUNCTION
# ________________________________________________
# x = [1, 2, 3]
# y = [4, 5, 6]
#
# c = [i * j for i, j in zip(x, y)]
# print(c)


# multiply to reverse version of list
# x = [1, 2, 3]
# y = [i * j for i, j in zip(x, reversed(x))]
# count how many tuples are open
# x = '(((((((((((())))()(()()())))))))))'
#
# if x.count('(') == x.count(')'):
#     print('ok')

########################################
# #_________________________________________________________________________________________________
# import random
#
#
# def get_random_list(n=20, a=0, b=20):
#     """ function to generate n sized list
#     of random numbers in a range of a to b"""
#
#     return [random.randint(a, b) for _ in range(n)]
#
#########################################################
# # 1. Find the most common element in an array of integers.
# arr = get_random_list()
# arr.sort()
# print(arr)
#
# counter = 0
# num = 0
# for i in arr:
#     frequency = arr.count(i)
#     if frequency > counter:
#         counter, num = frequency, i
#
# print(num, counter)
###########################################################
#
# # 2. Find the maximum number of identical elements in this array.
#
# arr = get_random_list()
# arr.sort()
# print(arr)
#
# print(max([arr.count(i) for i in arr]))
#
# counter = 0
# for i in arr:
#     frequency = arr.count(i)
#     if frequency > counter:
#         counter = frequency
#
# print(counter)
#
# # 3. Find the number of distinct elements in a given array.
#
# arr = get_random_list()
# print(arr)
# result = []
#
# for i in arr:
#     if arr.count(i) == 1:
#         result.append(i)
#
# print(len(result))
#
# print(len([i for i in arr if arr.count(i) == 1]))
#
# # --------------------------------------------------
#
# # - Given an array, divide it into n-sized chunks ->
# arr = [1, 2, 3, 4, 5, 6, 7]
# n = 3
# result = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7]
#


