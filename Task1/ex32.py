int1 = int(input("Enter the first number: "))
int2 = int(input("Enter the second number: "))
int3 = int(input("Enter the third number: "))

print("\nThe minimal number is -- " + str(min(int1, int2, int3)))
print("The middle number is -- " + str( (int1 + int2 + int3) - min(int1, int2, int3) - max(int1, int2, int3) ))
print("The maximal number is -- " + str(max(int1, int2, int3)))