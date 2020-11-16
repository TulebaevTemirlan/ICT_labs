# from collections import OrderedDict 
# s = str(input("Enter your string - "))
# s1 = "".join(OrderedDict.fromkeys(s))  
# dic1 = {}
# cnt = 0
# for i in range(0, len(s1)):
#     dic1.update({i : s1[i]})
#     cnt += 1
# print("Here is/are " + str(cnt) + " unique characters")
# Another solution

s = str(input("Enter your word/words - "))
dic1 = {}
dic2 = {}
cnt = 0
for i in range(0, len(s)):
    dic1.update({i : s[i]})
for key,value in dic1.items():
    if value not in dic2.values():
        dic2[key] = value
        cnt += 1
print("Here is/are " + str(cnt) + " unique character/charcters")