import math

n = int(input())
i = 1
# math.sqrt(n) - makes n float ,so int() will turn it to intger type.
# and math.sqrt(n) + 1 make accurate border to while loop
while(i < int(math.sqrt(n)) + 1):
    print(i**2)
    i += 1