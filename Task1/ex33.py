number_of_breads = float(input("Enter the number of breads you want to buy: "))

discount = 60
price = 3.49

answer = number_of_breads * price * ((100 - discount) / 100)

print("\nThe regular price is -- $ " + "{0:.2f}".format(int(number_of_breads * price)))
print("The discount is -- " + str(discount) + " %")
print("The total price with discount is -- $ " + "{0:.2f}".format(int(answer)))