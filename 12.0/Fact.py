import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)


def fact(n):
    a = 1
    if n==0 or n==1:
        return 1
    else:
        for i in range(2, n+1):
            a = a*i
    return a


N = int(input())
for i in range(N):
    line = input()
    B = int(line.split()[0].strip())
    N = int(line.split()[1].strip())
    k = 0
    while True:
        f = fact(k)
        n = int2base(f, B)
        s = str(n)




        k +=1

