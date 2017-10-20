import math

l = int(input())
alp_size = 26

alphabet = {}
for i in range(alp_size):
    letter_line = list(input().split(" "))
    alphabet[letter_line[0]] = float(letter_line[1])*math.pi/180
phrase = input()
phrase = ''.join(filter(str.isalpha, phrase))
phrase = phrase.upper()
phrase_list = list(phrase)
length = l
for i in range(len(phrase_list)-1):
    theta = abs(alphabet[phrase_list[i]] - alphabet[phrase_list[i+1]])
    inverse_theta = 2*math.pi - theta
    small_theta = 0
    if(theta < inverse_theta):
        small_theta = theta
    else:
        small_theta = inverse_theta
        
    small_theta = small_theta/2
    s = 2*l*math.sin(small_theta)
    length = length + s
print(int(round(length)))
    
    
