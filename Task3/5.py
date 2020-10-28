s = str(input())
s = ''.join(set(s))
answer = 0
for i in range(0, len(s)):
    answer += 1

if(answer % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM")
