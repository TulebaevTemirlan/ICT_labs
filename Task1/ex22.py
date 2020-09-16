# Let s = (s1 +s2 +s3)/2. Then the area of the triangle can be calculated using the
#  	following formula: area =√(s×(s-s1)×(s-s2)×(s-s3))

import math

s1 = int(input("Enter the first side of the triangle: "))
s2 = int(input("Enter the second side of the triangle: "))
s3 = int(input("Enter the third side of the triangle: "))

s = (s1 + s2 + s3) / 2

area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

print("\nThe area of the triangle: " + str(area))