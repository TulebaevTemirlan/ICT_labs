lst = []
n = int(input())
x = 0
answer = 0
lst = list(map(int, input().split()))
lst.sort()
i = 1
for i in range(len(lst)):
    if(lst[i - 1] == lst[i]):
        answer += 1
#print(lst)
print(answer)