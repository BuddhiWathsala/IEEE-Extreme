import math

n = int(input())
arr = input()
arr = [int(i.strip()) for i in arr.split()]
arr.sort()
A = sum(arr)/n
avg1 = math.floor(A)
avg2 = math.ceil(A)
I1 = math.floor(n/2)
I2 = math.ceil(n/2)
l1 = [0]*n
l2 = [0]*n
l3 = [0]*n
l4 = [0]*n
k = 0
for j in range(I1, n):
    l1[j] = avg1 + k
    k += 1

k = 1
for j in range(I1-1, -1, -1):
    l1[j] = avg1 - k
    k += 1

k = 0
for j in range(I1, n):
    l2[j] = avg2 + k
    k += 1

k = 1
for j in range(I1-1, -1, -1):
    l2[j] = avg2 - k
    k += 1

############################

for j in range(I2, n):
    l3[j] = avg1 + k
    k += 1

k = 1
for j in range(I2-1, -1, -1):
    l3[j] = avg1 - k
    k += 1

k = 0
for j in range(I2, n):
    l4[j] = avg2 + k
    k += 1

k = 1
for j in range(I1-1, -1, -1):
    l4[j] = avg2 - k
    k += 1
x1 = 0
x2 = 0
x3 = 0
x4 = 0
for i in range(n):
    x1 = x1 + abs(l1[i]-arr[i])
    x2 = x2 + abs(l2[i]-arr[i])
    x3 = x3 + abs(l3[i]-arr[i])
    x4 = x4 + abs(l4[i]-arr[i])
print(min(x1, x2, x3, x4))
