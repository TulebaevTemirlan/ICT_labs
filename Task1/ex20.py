pressure = float(input("Enter the measurement of pressure: "))
volume = float(input("Enter the volume: "))
temperature = float(input("Enter the temperature: "))
R = 8.314
#PV =nRT 

n = (pressure * volume) / (R * temperature)
Na = 6.02 * 10**23
mol = n / Na 
print("\n" + str(Na))
print(mol)