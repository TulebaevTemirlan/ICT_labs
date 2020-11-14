num = int(input())

numbers = {1: "one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

numbers_teen = {1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"}

numbers_ten = {1:"ten", 2:"twenty", 3:"thirty", 4:"fourty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

numbers_hundred = {1:"one hundred", 2:"two hundred", 3:"three hundred", 4:"four hundred", 5:"five hundred",
                     6:"six hundred", 7:"seven hundred", 8:"eight hundred", 9:"nine hundred"}

def fromIntToString(num):
    s_num = ""
    if(num == 0):
        s_num = "zero"
    elif(num < 10): # like 3, 4, 5, 6
        s_num += numbers[num]
    elif(num > 10 and num < 20): # like 13, 14, 15, 16
        s_num += numbers_teen[num % 10]
    elif(num < 100 and num % 10 == 0): # like 40, 50, 60
        s_num += numbers_ten[num // 10]
    elif(num < 100 and num % 10 != 0): # like 32, 45, 56, 67
        s_num += numbers_ten[num // 10] + " " + numbers[num % 10]
    elif((num % 100) % 10 == 0 and (num % 100) // 10 == 0): # like 400, 500, 600
        s_num += numbers_hundred[num // 100]
    elif(num > 100 and num % 100 > 10 and num % 100 < 20): # like 419, 513, 617
        s_num += numbers_hundred[num // 100]  + " " + numbers_teen[num % 10]
    elif((num % 100) % 10 == 0): # like 430, 530, 630
        s_num += numbers_hundred[num // 100] + " " + numbers_ten[(num % 100) // 10]
    elif((num % 100) // 10 == 0): # like 403, 502, 604
        s_num += numbers_hundred[num // 100] + " " + numbers[(num % 100) % 10]
    else: # like 342, 354, 756
        s_num += numbers_hundred[num // 100] + " " + numbers_ten[(num % 100) // 10] + " " + numbers[(num % 100) % 10]
    print(s_num)

fromIntToString(num)