import math

seconds = int(input("Enter the number of seconds: "))

days = seconds / 86400
hours = (seconds % 86400) / 3600
minutes = (seconds % 86400 % 3600) / 60
seconds = (seconds % 86400 % 3600 % 60) / 1

print("\n{0:.0f}".format(int(days)) + " : " + "{0:.0f}".format(int(hours)) + " : " + "{0:.0f}".format(int(minutes)) + " : " + "{0:.0f}".format(int(seconds)))
