#area =n× s^2/( 4×tg(π/n) )

import math

n = float(input("Enter the number of sides: "))
l = float(input("Enter the length of a side: "))

area = n * (l**2 / (4 * math.tan(math.pi / n)))

print("\nThe area of a regular polygon is: " + str(area))