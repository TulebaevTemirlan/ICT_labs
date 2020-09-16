integer = int(input("Enter your four digits number: "))

answer = (integer / 1000) + (integer % 1000 / 100) + (integer % 1000 % 100 / 10) + (integer % 10)

print("\nYour answer is -- " + "{0:.0f}".format(int(answer)))