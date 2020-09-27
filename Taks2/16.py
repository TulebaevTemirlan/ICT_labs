i = 1
prev = 0
answer = 0
maxi = 0
while(i > 0):
    current = int(input())
    if(current == 0):
        break
    if(current > prev):
        prev = current
        maxi = current
    if(current < prev):
        answer += 1
print(answer)

# not right solution for this problem