def rotate(l, n):
    return int(l[-n:]) + int(l[:-n])

lst = []

prev = 0
n = int(input())
lst1 [n]
lst = list(map(int, input().split()))
#print(rotate(lst, 1))
for i in range(len(lst)):
    if(i == 0):
        # prev = int(lst[n])
        # nex = int(lst[i + 1])
        lst1[i] = int(lst[n - 1])
    if(i == n - 1):
        # prev = int(lst[i - 1])
        # nex = int(lst[0])
        lst1[n - 1] = int(lst[0])
    else:
        # prev = int(lst[i - 1])
        # nex = int(lst[i + 1])
        lst1[i] = int(lst[i + 1])
    for i in range(len(lst1)):
        print(lst1[i], " ")

# I DID NOT SOLVE THIS PROBLEM