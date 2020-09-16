import math

radius = float(input("Enter radius of a cylinder: "))
height = float(input("Enter height of a cylinder: "))

volume = math.pi * 2 * radius * height

print("\nThe volume of the cylinder is " + "{0:.1f}".format(float(volume)))