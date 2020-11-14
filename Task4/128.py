def reverse_Lookup(dic, value):
    dicReturn = {}
    for key in dic:
        if(dic[key] == value):
            dicReturn[key] = value
    return dicReturn

dic1 = {"salary": 25, "age": 5, "number": 3}
print(reverse_Lookup(dic1, 25))

dic2 = {"salary of engineer": 250000, "salary of writer": 50000, "salary of dancer": 30000}
print(reverse_Lookup(dic2, 4000))

dic3 = {"age of Ben": 5, "age of Sarah": 5}
print(reverse_Lookup(dic3, 5))