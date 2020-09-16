small = int(input("How many small containers do you have ?"))
large = int(input("How many large containers do you have ?"))

refund = (small * 0.10) + (large * 0.25)

print("The total refund is $" + "{0:.2f}".format(float(refund)))