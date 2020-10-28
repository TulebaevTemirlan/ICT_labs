s = str(input())
teamA = 0
teamB = 0
answer = "NO"
for i in range(0, len(s)):
    if(teamA == 7 or teamB == 7):
        answer = "YES"
    if(s[i] == "0"):
        teamA += 1
        teamB = 0
    elif(s[i] == "1"):
        teamA = 0
        teamB += 1

print(answer)