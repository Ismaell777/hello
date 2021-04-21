# 1
x = []
i = 0
n = 10

while i < n:
    if i == 0 or i == 9:
        x.append(1)
    else:
        x.append(0)
    i += 1

print(x)

# 2
x = []
i = 0
n = 10

while i < n:
    if i % 2 == 0:
        x.append(0)
    else:
        x.append(1)
    i += 1

print(x)

# 3
x = []
i = 0
n = 10

while i < n:
    if i % 2 == 1:
        x.append(i)
    i += 1

print(x)

# 5
x = []
i = 0
n = 10

while i < n:
    if i % 2 == 0:
        x.append(i)
    i += 1

print(x)

# 6
x = []
i = 30

while i >= 0:
    if i % 3 == 0:
        x.append(i)
    i -= 1

print(x)

# 19
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = 5

print(a in x)

# 20
x = [3, 7, 5, 44, 33, 6, 2, 9, 8, 1]
i = 0
counter = 0

while i < len(x):
    if i % 2 == 0:
        counter += 1
    i += 1

print(counter)

# 21
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 14]
i = 0
counter = 0

while i < len(x):
    if i % 3 == 0 and i % 7 != 0:
        counter += 1
    i += 1

print(counter)

# 22
x = [2, 3, 6, 7, 8, 5]
i = 0
counter = 0

while i < len(x):
    if i % 2 == 0:
        counter += x[i]
    i += 1
    if i % 5 == 0:
        counter += x[i]
    i += 1

print(counter)

# 23
x = [2, 3, 4, 5, 6, 7, 8, 9]
i = 0
counter = 0

while i < len(x):
    counter += x[i]
    i += 1

print(counter)

# 24
x = [2, 3, 4, 5, 6, 7, 8, 9]
i = 0
counter = 0

while i < len(x):
    if x[i] % 2 == 0:
        counter += x[i]
    i += 1

print(counter)

# # list comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

