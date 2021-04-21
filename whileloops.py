"""
#76
n = int(input('enter number: '))

while n > 0:
    print('silence is golden')
    n -= 1

#77
n = int(input('enter number: '))


while n > 0:
    print('00000')
    n -= 1

#78
n = int(input('enter number: '))
i = n

while n > 0:
    print('*' * n)
    i -= 1


#79
i = 1

while i <= 20:
    print(i)
    i += 1

#80
n = 1001

while n <= 1025:
    print(n)
    n += 3

#81
n = 100

while n >= 0:
    print(n)
    n -= 4


#82
n = 1.2

while n <= 2.8:
    print(n)
    n += 0.2

#83
i = 25

while i <= 35:
    print(i, i + .5, i - .2)
    i += 1
#84
i = 1

while i <= 100:
    print(i, i * 70, i * 3.5)
    i += 1

#86
n = int(input('enter number: '))

i = 1
result = 0

while i <= n:
    result += i
    i += 1
print(result)

#87

start = 10
end = 88
result = 0

while start <= end:
    result += start
    start += 1
print(result)

#88
start = 5
end = 13
result = 1

while start <= end:
    result *= start
    start += 1
print(result)

#89
start = 0
end = 112

while start <= 112:
    result += start
    start += 4
print(result)


#90
import math

start = 3
end = 113
result = 0

while start <= end:
    result += math.cos(start / start + 2)
    start += 2
print(result)

#91
start = 2
end = 10
result = 0

while start <= end:
    result += start / start + 2
    start += 1
print(result)

#92
start = 1
end = 100
result = 0

while start <= end:
    result += start
print(result)

#93
start = 1
n = int(input('enter number'))
result = 0

while start <= n:
    result += n ** 2
    start += 1
print(result)

#94
start = 1
n = int(input('enter number'))
result = 0

while start <= 1:
    result += 1 / start
    start += 1
print(result)

#95
start = 1
a = int(input('enter number'))
n = int(input('enter number'))
p = 1

while start <= n:
    p *= (a + start) ** 2
    start += 1
print(start)


#96
import math

start = 1
x = int(input('enter number'))
n = int(input('enter number'))
result = 0

while start <= n:
    result += start / math.cos(x ** 2)
    start += 1
print(result)

#97
start = 1
n = int(input('enter n'))
result = 0

while start <= n:
    result += n * (n + start) * 2 * n
    start += 1
print(result)
"""
#