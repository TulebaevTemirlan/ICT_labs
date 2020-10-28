n = int(input())
s = str(input())

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'u', 'w', 'x', 'y', 'z']
if(n >= 26):
    for i in range(0, len(s)):
        s[i] = s[i].lower()
        if(s[i] in lst):
            s = s[:i] + s[i + 1:]
print(s)
#---------------------------