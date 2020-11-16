s1 = str(input("Enter first word - "))
s2 = str(input("Enter second word - "))
dic1 = {}
dic2 = {}
s1 = sorted(s1)
s2 = sorted(s2)
cnt = 0
if(len(s1) != len(s2)):
    print("They can't be anagrams of each other, lengthes not equal")
else:
    for i in range(0, len(s1)):
        dic1.update({i : s1[i]})
    for i in range(0, len(s2)):
        dic2.update({i : s2[i]})
    for key in dic1:
        if(dic1[key] != dic2[key]):
            print("They can't be anagrams of each other")
            break
        else:
            cnt += 1
if(cnt == len(s1)):
    print("They are anagrams of each other")
    
