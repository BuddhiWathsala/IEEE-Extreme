def manhatten(p1,p2):
    return (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))

line = list(input().split())
k = int(line[2])
matrix = []
counts = []
for i in range(k):
    L = list(input().split())
    L = list(map(int, L))
    matrix.append(L)
    counts.append(0)
for i in range(len(matrix)):
    l = matrix[i]
    for j in range(i+1,len(matrix)):
        current_l = matrix[j]
        m = manhatten(l,current_l)
        if(m <= l[2]):
            counts[j] = counts[j] + 1
        elif(m <= current_l[2]):
            counts[i] = counts[i] + 1
        else:
            continue
max_val = max(counts)
print(str(counts.index(max_val)+1)+ " "+ str(max_val))
        
    
    
    
