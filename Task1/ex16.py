# Hint: The area of a circle is  area = πr2.
# The volume of a sphere is  volume= 4 3πr3.
import math

r = float(input("Enter the radius: "))
area = math.pi * (r**2)
volume = math.pi * (r ** 3)

print("\nThe area of a circle is " + str(area))
print("The volume of a sphere is " + str(volume))
