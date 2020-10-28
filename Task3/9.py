n = int(input())
s = str(input())
anton = 0
danik = 0
for i in range(0, n):
    if(s[i] == "A"):
        anton += 1
    else:
        danik += 1
if(anton > danik):
    print("Anton")
elif(danik > anton):
    print("Danik")
elif(danik == anton):
    print("Friendship")