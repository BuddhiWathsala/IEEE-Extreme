import numpy

t = int(input())
for i in range(t):
    L = list(input().split())
    L = list(map(int, L))
    W = L[0]
    N = L[1]
    matrix = []
    for j in range(N):
        l = list(input().split())
        l = list(map(int, l))
        matrix.append(l)
    matrix = sorted(matrix,key=lambda x: x[0])
    
    w = 0
    val = 0
    M = numpy.zeros(shape=(N,W+1))

    for j in range(1,W+1):
        M[0][j] = matrix[0][1]
    for j in range(1,N):
        cur_val = matrix[j][1]
        cur_w = matrix[j][0]

        for k in range(1,W+1):
            if(k<cur_w):
                M[j][k] = M[j-1][k]
            else:
                M[j][k] = max(cur_val+M[j-1][k-cur_w],M[j-1][k])
    print(int(M[j-1][W]))
            
        
