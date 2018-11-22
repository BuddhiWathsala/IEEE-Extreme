T = int(input())
A = []
for i in range(T):
    line1 = input()
    S = int(line1.split()[0].strip())
    E = int(line1.split()[1].strip())
    if E == 0:
        L = input()
        A.append(["!OK", ""])
        continue

    L = input()
    L = [int(n.strip()) for n in L.split()]

    flag = True
    for j in range(1, len(L)):
        if not flag:
            break
        for k in range(len(L)-j):
            l1 = L[k]
            l2 = L[j+k]
            if S == (l1+l2):
                if l1 > l2:
                    A.append([l2, l1])
                else:
                    A.append([l1, l2])
                flag = False
                break

    if flag:
        A.append(["!OK", ""])


for I in A:
    print(I[0], I[1])