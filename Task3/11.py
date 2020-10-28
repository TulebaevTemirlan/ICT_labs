m = int(input())
s = str(input())
z = 0
e = 0
r = 0
o = 0
n = 0

for i in range(0, len(s)):
    if(s[i] == 'z'):
        z += 1
    elif(s[i] == 'e'):
        e += 1
    elif(s[i] == 'r'):
        r += 1
    elif(s[i] == 'o'):
        o += 1
    elif(s[i] == 'n'):
        n += 1
while(z > 0 or e > 0 or r > 0 or o > 0 or n > 0):
    if(o > 0 and n > 0 and e > 0):
        o -= 1
        n -= 1
        e -= 1
        print(1, end= " ")
    else:
        z -= 1
        e -= 1
        r -= 1
        o -= 1
        print(0, end=" ")
