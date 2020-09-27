lst = []
answer = 0
n = int(input())
lst = input().split()
i = 1
for i in range(0,len(lst)):
    if(int(lst[i - 1]) != int(lst[i])):
        answer += 1
print(answer)