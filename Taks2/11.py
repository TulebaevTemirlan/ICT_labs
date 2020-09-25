n = int(input());
# this range starts from 2 and end by n + 1, because in python range include first border , but not include last one
for i in range(2,n + 1): 
    if(n % i == 0):
        print(i)
        break
