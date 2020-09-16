cost_of_meal = float(input("How much your meal is costs ?"))
tax = cost_of_meal * 0.12
tip = cost_of_meal * 0.18
grand_total = cost_of_meal + tax + tip

#print("{0:.2f}".format(float(tax)))
#print(format(str(tax)) + " " + format(str(tip)))

print("The amount of the tax is " + "{0:.2f}".format(float(tax)) + " tenge.")
print("The amount of the tip is " + "{0:.2f}".format(float(tip)) + " tenge.")
print("The grand total amount for the meal including tax and tip is " + "{0:.2f}".format(float(grand_total)) + " tenge.")
