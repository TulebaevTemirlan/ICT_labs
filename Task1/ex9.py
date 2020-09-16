money = int(input("Enter the number of money: "))
# profit = money * 0.04
# after1 = money + profit
# money = after1
print("\n")
for i in range(3):
    profit = money * 0.04
    after1 = money + profit
    print("Money in the savings account after " + str(i + 1) + " year/years is " + "{0:.2f}".format(float(after1)))
    money = after1
