import numpy      


def isValid(main_matrix,h,w):
    val = min(h,w)
    for i in range(3,val+1):
        for j in range(h-i+1):
            for k in range(w-i+1):
                sub = main_matrix[j:j+i,k:k+i]
                non_zero = numpy.nonzero(sub)
                number_non_zero = len(non_zero[0])
                if(number_non_zero > (i-1)):
                    return("NO")
                    
    return("YES")
ans = []
t = int(input())


for i in range(t):
    line = list(input().split(' '))
    h = int(line[0])
    w = int(line[1])
    metrix = []
    
    for j in range(h):
        row_str = input()
        row_str = row_str.replace('.','0')
        row_list = list(map(int, row_str))
        metrix.append(row_list)
    metrix = numpy.matrix(metrix)
    
    b = isValid(metrix,h,w)
    
    ans.append(b)
for j in ans:
    print(j)
    


