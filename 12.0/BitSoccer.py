N = int(input())
p_players = input()
p_players = [int(n.strip()) for n in p_players.split()]
S = 0
for i in range(N-1):
    temp = p_players[i] | p_players[i+1]
    S = temp | S

Q = int(input())

for i in range(Q):
    num = int(input())
    val = S & num
    if val > 0:
        print("YES")
    else:
        print("NO")
