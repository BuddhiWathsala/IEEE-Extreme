import math

l = input()
A = int(l.split()[0].strip())
B = int(l.split()[1].strip())

x = math.ceil((2**B)/A)
print(x)