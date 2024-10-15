a = 5
b = 10
temp = a
a = b
b = temp
print(a)
print(b)

a = 5
b = 10
a, b = b, a
print(a)
print(b)

a = 5
b = 10
a = a + b
b = a - b
a = a - b
print(a)
print(b)

a = 5
b = 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)
