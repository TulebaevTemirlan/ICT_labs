import math

n = int(input())
i = 0
num = 1
# math.sqrt(n) - makes n float ,so int() will turn it to intger type.
# and math.sqrt(n) make accurate border to while loop
#I used num variable instead of i , because when while loop starts with i , then it prints one more integer as output and more than n
while(num < int(math.sqrt(n))):
    print(2**i)
    i += 1
    num += 1