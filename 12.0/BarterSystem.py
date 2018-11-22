import math

INF = math.inf
M = 998244353
N = int(input())
lst = []
tuples = []
for i in range(N):
    line = input().split()
    s1 = line[0]
    s2 = line[1]
    num = int(line[2])
    tuples.append([s1, s2, num])
    if s1 not in lst:
        lst.append(s1)
    if s2 not in lst:
        lst.append(s2)

matrix = []
for i in range(len(lst)):
    s = [INF]*len(lst)
    matrix.append(s)
for i in range(len(lst)):
    matrix[0][0] = 0
for l in tuples:
    i = lst.index(l[0])
    j = lst.index(l[1])
    matrix[i][j] = l[2]


for k in range(len(lst)):
    for i in range(len(lst)):
        for j in range(len(lst)):
            x = (matrix[i][k]*matrix[k][j])%M
            if (x != 0) and (matrix[i][j] > x):
                matrix[i][j] = x

TN = int(input())
answer = []
for i in range(TN):
    line = input().split()
    indexI = lst.index(line[0].strip())
    indexJ = lst.index(line[1].strip())
    if indexJ == indexI:
        answer.append(1)
        continue
    value = matrix[indexI][indexJ]
    if value == 0:
        value = -1
    answer.append(value)

for i in answer:
    if i == INF:
        print(-1)
    else:
        print(i)
