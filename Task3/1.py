s = str(input())

for i in range(0,len(s)):
    if(s[i] == "a" or s[i] == "o" or s[i] == "y" or s[i] == "e" or s[i] == "u" or s[i] == "i"):
        s = s[:i] + "." + s[i + 1:]
    elif(s[i] == "A" or s[i] == "O" or s[i] == "Y" or s[i] == "E" or s[i] == "U" or s[i] == "I"):
        s = s[:i] + "." + s[i + 1:]
    elif(s[i] == s[i].upper()):
        s = s[:i] + s[i].lower() + s[i + 1:]
print(s)