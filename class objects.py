# class Cars:
#     def __init__(self, model, petrol):
#         self.model = model
#         self.petrol = petrol
#         self.location = None
#
#     def car_model(self):
#         return self.model
#
#     def petrol_type(self):
#         return self.petrol
#
#     def print_data(self):
#         print(self.location, self.model, self.petrol)
#
#
# class Mercedes(Cars):
#     def __init__(self, model, petrol):
#         super().__init__(model, petrol)
#         self.location = 'GERMANY'
#
#
# class Lexus(Cars):
#     def __init__(self, model, petrol):
#         super().__init__(model, petrol)
#         self.location = 'JAPAN'
#
#
# class Ford(Cars):
#     def __init__(self, model, petrol):
#         super().__init__(model, petrol)
#         self.location = 'United States'
#
#
# def list_data(data):
#     for i in data:
#         i.print_data()
#
#
# cars = [
#     Mercedes('AMG', 91),
#     Lexus('Sport', 90),
#     Ford('Mustang', 95),
# ]
#
# list_data(cars)
#
#
# #######################################
#
# class Animal:
#     def __init__(self, f_amount, name):
#         self.amount = f_amount
#         self.name = name
#         self.type = None
#
#     def food_amount(self):
#         return self.amount
#
#     def food_type(self):
#         return self.type
#
#     def print_data(self):
#         print(self.name, self.type, self.amount)
#
#
# class Carnivore(Animal):
#     def __init__(self, f_amount, name):
#         super().__init__(f_amount, name)
#         self.type = 'meat'
#
#
# class Omnivore(Animal):
#     def __init__(self, f_amount, name):
#         super().__init__(f_amount, name)
#         self.type = 'mix'
#
#
# class Herbivore(Animal):
#     def __init__(self, f_amount, name):
#         super().__init__(f_amount, name)
#         self.type = 'herbs'
#
#
# def list_data(data):
#     for i in data:
#         i.print_data()
#
#
# animals = [
#     Carnivore(10, 'Tiger'),
#     Omnivore(5, 'Grizzly'),
#     Herbivore(15, 'Cow'),
#     Carnivore(10, 'Wolf'),
#     Carnivore(12, 'Lion'),
#     Carnivore(8, 'Cheetah'),
#     Carnivore(6, 'Panther'),
# ]
#
# animals.sort(key=lambda i: (i.food_amount(), i.name), reverse=True)
#
# # for i in animals[:5]:
# #     print(i.name)
#
# animals = animals[:-3]
#
# # for i in range(5):
# #     print(animals[i].name)
#
# list_data(animals)
#
#
# ####################################################
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'<{self.x}, {self.y}>'
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, other):
#         if isinstance(other, Vector):
#             return self.x * other.x + self.y * other.y
#         else:
#             return Vector(self.x * other, self.y * other)
#
#
# a = Vector(4, 2)
# b = Vector(1, 0)
#
# print(a * b)
# print(a * 5)
# ################################################
#
# from math import pi
#
#
# class Figure:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def perimeter(self):
#         pass
#
#     def area(self):
#         pass
#
#     def print_info(self):
#         pass
#
#
# class Circle(Figure):
#     def __init__(self, r):
#         super().__init__(r, None)
#
#     def perimeter(self):
#         return 2 * pi * self.a
#
#     def area(self):
#         return pi * self.a ** 2
#
#
# #
# class Square(Figure):
#     def __init__(self, a):
#         super().__init__(a, None)
#
#     def perimeter(self):
#         return self.a * 4
#
#     def area(self):
#         return self.a * self.a
#
#
# s1 = Square(4)
#
#
# class Rectangle(Figure):
#     def perimeter(self):
#         pass
#
#     def area(self):
#         pass
#
#     def print_info(self):
#         pass
#
#
# #
# class Triangle(Figure):
#     def __init__(self, a, b, c):
#         super().__init__(a, b)
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# t1 = Triangle(3, 4, 5)
#
#
# class Car:
#     def __init__(self, model, made_cn):
#         self.model = model
#         self.made_cn = made_cn
#
#     def print_name(self):
#         print(self.model, self.made_cn)
#
#
# class Truck(Car):
#     def __init__(self, model, made_cn, year):
#         super().__init__(model, made_cn)
#         self.made_date = year
#
#     def selam(self):
#         print('this is new model of ', self.model, 'was made in ', self.made_cn, 'in ', self.made_date)
#
#
# x = Truck('Mercedes - Benz', 'Germany', 2021)
# x.selam()
#
#
# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance(self, other):
#         x_diff_sq = (self.x - other.x) ** 2
#         y_diff_sq = (self.y - other.y) ** 2
#         return (x_diff_sq + y_diff_sq) ** 0.5
#
#     def __str__(self):
#         return "<" + str(self.x) + "," + str(self.y) + ">"
#
#
# t = Coordinate(1, 2)
# print(str(t))
#
# class Line:
#     def __init__(self, color1, color2):
#         self.color1 = color1
#         self.color2 = color2
#
#     def distance(self):
#         x1, y1 = self.color1
#         x2, y2 = self.color2
#
#         return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#
#     def slope(self):
#         x1, y1 = self.color1
#         x2, y2 = self.color2
#
#         return (y2 - y1) / (x2 - x1)
#
#
# coordinate1 = (3, 2)
# coordinate2 = (8, 10)
#
# myline = Line(coordinate1, coordinate2)
#
# print(myline.slope())


