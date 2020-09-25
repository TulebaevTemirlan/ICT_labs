a = int(input());
b = int(input());
c = int(input());

if((a <= b) and (a <= c)):
    first = a;
    if(b <= c):
        second = b;
        third = c;
    else:
        second = c;
        third = b;
elif((b <= a) and (b <= c)):
    first = b;
    if(a <= c):
        second = a;
        third = c;
else:
    first = c;
    if(a <= b):
        second = a;
        third = b;
    else:
        second = b;
        third = a;
print(str(first) + " " + str(second) + " " + str(third));

