s = str(input())

one = 0
two = 0
three = 0

for i in range(0, len(s)):
    if(s[i] == "1"):
        one += 1
    elif(s[i] == "2"):
        two += 1
    elif(s[i] == "3"):
        three += 1
while(one > 0 or two > 0 or three > 0):
    if(one > 0):
        if(one == 1 and two == 0 and three == 0):
            print("1")
        else:
            print("1", end="+")
        one -= 1
    elif(two > 0):
        if(one == 0 and two == 1 and three == 0):
            print("2")
        else:
            print("2", end="+")
        two -= 1
    else:
        if(one == 0 and two == 0 and three == 1):
            print("3")
        else:
            print("3", end="+")
        three -= 1