# # LAMBDA FUNCTION
#
# #  sort the string with the second item
# x = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# x.sort(key=lambda i: i[1])
#
# print(x)
#
# x = ['John Wick', 'Alice Robertson', 'Charlie Bacon', 'Sherlock Holmes']
# x.sort(key=lambda i: i.split()[1])
#
# print(x)
#
#
# # 2 write a Python program to create  a function that takes one argument, and that argument will be multiplied with an
# # unknown given number
#
# def func_compute(n):
#     return lambda x: x * n
#
#
# result = func_compute(2)
# print(result(9))
# result = func_compute(3)
# print(result(9))
# result = func_compute(4)
# print(result(9))
#
# # write a python program to sort a list of tuples using Lambda ['number']
# tpl = [('English', 88), ('Science', 90), ('Math', 97), ('Social sciences', 82)]
# tpl.sort(key=lambda i: i[1])
# print(tpl)
#
# # 4 Write a Python program to sort a list of dictionaries using Lambda ['color']
# lst = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# lst.sort(key=lambda i: i['color'])
# print(lst)
#
# # 5 write a Python program to filter a list of integers using Lambda
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda x: x % 2 == 0, lst))
# print(even_nums)
# odd_numbers = list(filter(lambda x: x % 2 == 1, lst))
# print(odd_numbers)
#
# # 6 Write a Python program to square and cube every number in a given list of integers using lambda
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square_num = list(map(lambda x: x ** 2, nums))
# print(square_num)
# cube_nums = list(map(lambda x: x ** 3, nums))
# print(cube_nums)
#
# # 7 write a python program to find if a given string starts with a given character using lambda
# starts_with = lambda x: True if x.startswith('s') else False
# print(starts_with('sunshine'))
# starts_with = lambda x: True if x.startswith('h') else False
# print(starts_with('yellow'))
#
# # 11 write a python program to find intersection of two given arrays using Lambda

# array1 = [1, 2, 3, 5, 7, 8, 9, 10]
# array2 = [1, 2, 4, 8, 9, 10]
# print("original arrays: " + str(array1) + " " + str(array2))
# result = list(filter(lambda x: x in array1, array2))
# print("\nIntersection of the arrays", result)
#
# # 12 write a python program to rearrange positive and negative numbers in a given array using Lambda
# arr = [-1, 2, -3, 5, 7, 8, 9, -10]
# result = sorted(arr, key=lambda i: 0 if i == 0 else -1 / i)
# print(result)
# a python program to count the even, odd numbers in a given array
# array_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_nums = l
# # # # 13 writen(list(filter(lambda x: (x % 2 != 0), array_nums)))
# even_nums = len(list(filter(lambda x: (x % 2 == 0), array_nums)))
# print('original array:', array_nums)
# print('\nNumber of odd numbers: ', odd_nums)
# print('\nNumber of even numbers: ', even_nums)
#
# # find the solution of length six in a given list using lambda
# lst = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
# x = filter(lambda s: s if len(s) == 6 else '', lst)
# for d in x:
#     print(d)
# #
#
# class Person:
#     def __init__(self, f_name, l_name):
#         self.firstname = f_name
#         self.lastname = l_name
#
#     def print_name(self):
#         print(self.firstname, self.lastname)
#
#
# class Student(Person):
#     def __init__(self, f_name, l_name, year):
#         super().__init__(f_name, l_name)
#         self.graduation_year = year
#
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)
#
#
# x = Student("Mike", "Olsen", 2019)
# x.welcome()

import platform
x = platform.node()
print(x)
