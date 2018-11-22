def is_sub(s,p):
    j = 0
    for i in range(len(s)):
        if(p[j] == s[i]):
            j = j + 1
            if(j == len(p)):
                return True
    return False
            
def get_suf(s):
    l = len(s)
    lst = []
    for i in range(1,l+1):
        lst.append(s[l-i:l])
    return lst

s = input()
q = int(input())
ans = []
for i in range(q):
    sub = input()
    suffixes = get_suf(sub)
    count = 0
    for l in suffixes:
        if(is_sub(s,l)):
            count = count + 1
    ans.append(count)
for i in ans:
    print(i)
            
        
        
    
