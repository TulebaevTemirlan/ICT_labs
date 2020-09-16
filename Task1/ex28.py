import math

temperature = float(input("Enter the temperature of a wind in Celcius: "))
wind_speed = float(input("Enter the speed of a wind kilometers/hour: "))

WCI = 13.12+ 0.6215 * temperature - 11.37 * wind_speed**0.16 + 0.3965 * temperature * wind_speed**0.16 

print("\nThe Wind Chill Index is: " + str(round(WCI)))