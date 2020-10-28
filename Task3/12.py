n = int(input())
s = str(input())
cnt = 0
answer = 0
for i in range(0, len(s)):
    if(cnt > 2):
        cnt -= 1
        answer += 1
    if(s[i] == "x"):
        cnt += 1
    else:
        cnt = 0        
# if(cnt > 2):
#     while(cnt > 2):
#         s = s.replace("x", "", 1)
#         cnt -= 1
#         answer += 1

print(answer)
