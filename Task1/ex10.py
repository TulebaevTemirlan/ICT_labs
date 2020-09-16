# •	The sum of a and b
# •	The difference when b is subtracted from a
# •	The product of a and b
# •	The quotient when a is divided by b
# •	The remainder when a is divided by b
# •	The result of log10 a
# •	The result of ab
# Hint: You will probably ﬁnd the log10 function in the math module helpful for computing the second last item in the list.
import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("\nSum - " + str(a + b))
print("Difference - " + str(b - a))
print("Product - " + str(a * b))
print("Quotient - " + str(a / b))
print("Remainder - " + str(a % b))
print("Log10 a - " + str(math.log10(a)))
