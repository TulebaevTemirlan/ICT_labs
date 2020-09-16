height_meters = float(input("Enter your height in meters: "))
weight_kilograms = float(input("Enter your weight in kilograms: "))

bmi = weight_kilograms / height_meters**2

print("\nYour Body Mass Index is: " + str(bmi))
