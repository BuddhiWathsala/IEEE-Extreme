q = int(input())
ans = []
for i in range(q):
    line = list(input().split(' '))
    a = int(line[0])
    b = int(line[1])
    a_bin = "{0:b}".format(a)
    b_bin = "{0:b}".format(b)
    if(len(a_bin) == len(b_bin)):
        num = 0
        temp_a = a
        temp_b = b
        while(temp_a != temp_b):
            temp_a = temp_a >> 1
            temp_b = temp_b >> 1
            num = num + 1
        print(num*2)
    else:
        num = 0
        temp_max = max(a,b)
        temp_min = min(a,b)
        temp_max_bin_len = len("{0:b}".format(temp_max))
        temp_min_bin_len = len("{0:b}".format(temp_min))
        v = temp_max_bin_len - temp_min_bin_len
        num = 0
        temp_a = temp_max >> v
        temp_b = temp_min
        while(temp_a != temp_b):
            temp_a = temp_a >> 1
            temp_b = temp_b >> 1
            num = num + 1
        print(num*2 + v)
    

