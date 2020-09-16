import math

t1 = int(input("Enter latitude of the first point: "))
g1 = int(input("ENter longitude of the first point: "))
t2 = int(input("Enter latitude of the second point: "))
g2 = int(input("ENter longitude of the second point: "))

t1 = math.radians(t1)
g1 = math.radians(g1)
t2 = math.radians(t2)
g2 = math.radians(g2)

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

print("\n" + str(distance))