# Hint: The speciﬁc heat capacity of water is 4.186 J g◦C.
# Because water has a density of 1.0 gram per milliliter,
# you can use grams and milliliters interchangeably in this exercise.
# Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use your program to compute the cost of boiling water for a cup of coffee.

t = float(input("Enter the temperature change: "))
m = float(input("Enter the mass of water: "))
C = 4.186
q = m * C * t 

print("\n" + str(q))