# : Distance Units (inches, yards and miles)

feet = float(input("Enter the a measurement in feet: "))
inches = feet * 12
yards = feet * 0.33333333333333
miles = feet * 0.0001893939393939394

print("\n" + str(feet) + " feet is equal to " + str(inches) + " inches.")
print(str(feet) + " feet is equal to " + str(yards) + " yards.")
print(str(feet) + " feet is equal to " + str(miles) + " miles.")
