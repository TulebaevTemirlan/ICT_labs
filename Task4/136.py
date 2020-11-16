s1 = str(input("Enter first string")).lower()
s2 = str(input("Enter second string")).lower()
s1 = s1.replace(" ", "")
s2 = s2.replace(" ", "")
s1 = sorted(s1)
s2 = sorted(s2)
iterator = 0
cnt = 0
ignored_chars = [" ", ",", ".", "!", ":", ";", "'", "?", "/"]
dic1 = {}
dic2 = {}
for i in range(0, len(s1)):
    if(s1[i] not in ignored_chars):
        dic1.update({iterator: s1[i]})
        iterator += 1
iterator = 0
for i in range(0, len(s2)):
    if(s2[i] not in ignored_chars):
        dic2.update({iterator: s2[i]})
        iterator += 1
if(len(dic1) != len(dic2)):
    print("They can't be anagrams of each other, lengthes not equal")
else:
    for key in dic1:
        if(dic1[key] != dic2[key]):
            print("They can't be anagrams of each other")
            break
        else:
            cnt += 1
if(cnt == len(dic1)):
    print("They are anagrams of each other")
