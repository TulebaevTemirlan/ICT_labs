s1 = str(input("Enter first word - "))
s2 = str(input("Enter second word - "))
dic1 = {}
cnt = 0
if(len(s1) != len(s2)):
    print("They can't be anagrams of each other, lengthes not equal")
else:
    for i in range(0, len(s1)):
        dic1.update({i : s1[i]})
    for y in range(0, len(s2)):
        if(s2[y] not in dic1.values()):
            print("They can't be anagrams of each other")
            break
        else:
            cnt += 1
if(cnt == len(s1)):
    print("They are anagrams of each other")

