i = 1
maxi = 0
amount = 1
while(i > 0):
    n = int(input())
    if(n > maxi): # here I check numbers for max value in sequence.And if new maxi found I assign amount = 1
        maxi = n 
        amount = 1
    elif(n == maxi):# here if last number which is maxi equal to the next number in sequence amount increases to 1
        amount += 1
    if(n == 0):
        break
print(amount)

#-------------------------