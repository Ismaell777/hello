
a = float(input('enter first number: '))
b = float(input('enter second number: '))
operator = input('enter operator: ')

if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    print(a / b)
else:
    print('error')

#14
a = float(input('enter first number: '))
b = float(input('enter second number: '))
operator = input("enter operator: ")

if operator == '+':
    print(a + b)
elif operator == '*':
    print(a * b)
else:
    print('error')


#15
a = float(input('enter number'))
operator = input('enter operator: ')

if operator == '*2':
    print(a ** 2)
elif operator == '*3':
    print(a ** 3)
else:
    print('error')



#16
a = float(input('enter first number: '))
b = float(input('enter second number: '))
c = float(input('enter third number: '))
operator = input('enter operator: ')

if operator == 'a2':
    print(a * 2)
elif operator == 'b3':
    print(b * 3)
elif operator == 'c**2':
    print(c ** 2)
elif operator == 'sum':
    print(a * 2 + b * 3 + c ** 2)
else:
    print('error')


#17
a = float(input('enter first number: '))
b = float(input('enter second number: '))
c = float(input('enter third number: '))
operator = input('enter operator: ')

if operator == 'middle':
    print((a + b + c) / 2)
elif operator == '-':
    print(a ** 2 - c ** 2 - b ** 3)
else:
    print('error')


#18
a = float(input('enter number'))
operator = input('enter operator')

if operator == 'S':
    print(pow(a,2) + pow(a, 2))
elif operator == 'P':
    print(a + a + a + a)
else:
    print('error')


#41
a = int(input('enter number'))

if a > 100 or a < -100:
    print(0)
else:
    print(a * 1)

#42
a = int(input('enter number'))

if a > 2 or a < 5:
    print(a * 10)
elif a > 7 or a < 40:
    print(a * 100)
elif a > 3000 or a < 0:
    print(a * 3)
else:
    print(0)

#43
a = int(input('enter number'))

if a == 1:
    print("spring")
elif a == 2:
    print("summer")
elif a == 3:
    print("autumn")
elif a == 4:
    print("winter")
else:
    print("error")

#44
a = int(input('enter first number'))
b = int(input('enter second number'))
if a != 10 and b != 10 and a % 2 == 0:
    print(a + b)
else :
    print(0)

#45
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))

if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print('yes')
else:
    print('no')


#leap year
a = int(input('enter number'))

if a % 4 == 0:
    print('leap year')
else:
    print('not leap year')


#46
a = int(input('enter  first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))

if a % 5 == 0:
    print(a)
elif b % 5 == 0:
    print(b)
elif c % 5 == 0:
    print(c)
else:
    print('error')

#47
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))

if a > b and a > c:
    print("a is the biggest")
elif b > a and b > c:
    print("b is the biggest")
elif c > a and c > b:
    print("c is the biggest")
else:
    print('error')


#48
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))

if a > b > c or b > a > c:
    print(a + b)
elif a > c > b or c > a > b:
    print(a + c)
elif b > c > a or c > b > a:
    print(b + c)
else:
    print('error')


#49
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))
d = int(input('enter forth number'))

if a % 2 == 0 > b % 2 == 0 and a % 2 == 0 > c % 2 == 0 and a % 2 == 0 > d % 2 == 0:
    print("a is bigger")
elif b % 2 == 0 > a % 2 == 0 and b % 2 == 0 > c % 2 == 0 and b % 2 == 0 > d % 2 == 0:
    print("b is bigger")
elif c % 2 == 0 > a % 2 == 0 and c % 2 == 0 > b % 2 == 0 and c % 2 == 0 > d % 2 == 0:
    print('c is bigger')
elif d % 2 == 0 > a % 2 == 0 and d % 2 == 0 > b % 2 == 0 and d % 2 == 0 > c % 2 == 0:
    print('c is bigger')


#50
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))

if a == b or a == c or c == b:
    print('yes')
else:
    print('error')

#52
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))
d = int(input('enter forth number'))

if a > 5 and b > 5 and c % 6 == 0 and d % 3 == 0:
    print('yes')
else:
    print('error')



#53
a = int(input('enter first number'))
b = int(input('enter second number'))

if a > 30 or b > 30:
    print('yes')
else:
    print('no')


#54
a = int(input('enter first number'))
b = int(input('enter second number'))
c = int(input('enter third number'))

if a < 5 and b < 5 or a < 5 and c < 5 or b < 5 and c < 5:
    print('yes')
else:
    print('no')

#58
a = int(input('enter data'))
b = int(input('enter data'))

if a < b:
    print('yes')
else:
    print('no')

#59
n = int(input('enter a number'))

a = n % 10
b = (n // 10) % 10
c = (n // 100) % 10
d = n // 1000

if d > c > b > a:
    print('yes')
else:
    print('no')


#60
n = int(input('enter a number'))

a = n % 10
b = (n // 10) % 10
c = n // 100

result = a * 100 + b * 10 + c
print(result)






