s = str(input()).upper()
province = ""
address = ""
my_chars = ["A","B","C","E","G","H","J","K","L","M","N","P","R","S","T","V","X","Y"]

provinces = {'A': "Newfoundland", 'B': "Nova Scotia", 
                    'C': "Prince Edward Island", 'E': "New Brunswick", 
                    'G': "Quebec", 'H': "Quebec", 'J': "Quebec",
                    'K': "Ontario", 'L': "Ontario", 'M': "Ontario",
                    'N': "Ontario", 'P': "Ontario", 'R': "Manitoba",
                    'S': "Saskatchewan", 'T': "Alberta", 'V': "British Columbia",
                    'X': "Nunavut or Northwest Territories", 'Y': "Yukon" 
            }
if(s[0] not in my_chars):
    print("Error! Please check that you entered correct code of your PROVINCE")
else:
    province += provinces[s[0]]
    if(s[1] == '0'):
        address = "rural"
    else:
        address = "urban"
    print("Your province is " + province + ". Address is " + address)
        