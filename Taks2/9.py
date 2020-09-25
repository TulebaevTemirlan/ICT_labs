a1 = int(input());
b1 = int(input());
c1 = int(input());

a2 = int(input());
b2 = int(input());
c2 = int(input());

if((a1 <= a2 and a1 <= b2 and a1 <= c2) and (b1 <= a2 and b1 <= b2 and b1 <= c2) and (c1 <= a2 and c1 <= b2 and c1 <= c2)):
    print("The first box is smaller than the second one")
elif((a2 <= a1 and a2 <= b1 and a2 <= c1) and (b2 <= a1 and b2 <= b1 and b2 <= c1) and (c2 <= a1 and c2 <= b1 and c2 <= c1)):
    print("The first box is larger than the second one")
elif((a1 == a2))

# How to check boxes are equal or not ?