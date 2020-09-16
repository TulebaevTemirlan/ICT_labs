# 1 dollar is 100 cents
# 1 half dollar is 50 cents
# 1 quarter dollar is 25 cents
# 1 dime is 10 cents 
# 1 nickel is 5 cents
# 1 penny is 1 cent 

cents = int(input("Enter the number of cents: "))

toonie = cents / 200
loonie = (cents % 200) / 100
quater = (cents % 200 % 100) / 25
dime = (cents % 200 % 100 % 25) / 10
nickels = (cents % 200 % 100 % 25 % 10) / 5
penny = (cents % 200 % 100 % 25 % 5) / 1

#print(cents % 200)
print("\nYour change is: \n")
print("Toonies " + "{0:.0f}".format(int(toonie)))
print("Loonies " + "{0:.0f}".format(int(loonie)))
print("Quaters " + "{0:.0f}".format(int(quater)))
print("Dimes " + "{0:.0f}".format(int(dime)))
print("Nickels " + "{0:.0f}".format(int(nickels)))
print("Pennies " + "{0:.0f}".format(int(penny)))
