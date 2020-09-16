kilopascals = float(input("Enter the measurement of pressure in kilopascals: "))

psi = kilopascals * 10**3 * 0.000145038
atm = kilopascals / 101.325
millimetres_of_mercury = kilopascals * 10**3 / 133

print("\nPounds per inches -- " + str(psi))
print("Millimetres of mercury -- " + str(millimetres_of_mercury))
print("Atmosphere --" + str(atm))