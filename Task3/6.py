s = str(input())
cntLower = 0
cntUpper = 0
for i in range(0, len(s)):
    if(s[i] == s[i].lower()):
        cntLower += 1
    else:
        cntUpper += 1
if(cntLower >= cntUpper):
    for i in range(0, len(s)):
        s = s[:i] + s[i].lower() + s[i + 1:]
else:
    for i in range(0, len(s)):
        s = s[:i] + s[i].upper() + s[i + 1:]
print(s)
