s = str(input()).upper()
counter = 0
dic1 = {}
iterator = 1
my_chars = [".",",","?","!",":","A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
phone_buttons = {1: {1: ".", 2: ",", 3: "?", 4: "!", 5: ":"},
                 2: {1: "A", 2: "B", 3: "C"},
                 3: {1: "D", 2: "E", 3: "F"},
                 4: {1: "G", 2: "H", 3: "I"},
                 5: {1: "J", 2: "K", 3: "L"},
                 6: {1: "M", 2: "N", 3: "O"},
                 7: {1: "P", 2: "Q", 3: "R", 4: "S"},
                 8: {1: "T", 2: "U", 3: "V"},
                 9: {1: "W", 2: "X", 3: "Y", 4: "Z"},
                 0: {1: " "}
                }
for z in range(0, len(s)):
    for key in phone_buttons:
        for key1 in phone_buttons[key]:
            if(counter >= len(s)):
                break
            if(s[counter] not in my_chars):
                print("here")
                counter += 1
            if(phone_buttons[key][key1] == s[counter]):
                for i in range(0, key1):
                    dic1.update({iterator : key})
                    iterator += 1
                counter += 1

for key in dic1:
    print(dic1[key], end="")
#Hello, World! = 4433555555666110966677755531111