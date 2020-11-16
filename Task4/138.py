import random
def createBingoCard():
    card = {"B": [], "I": [], "N": [], "G": [], "O": []}
    minn = 1
    maxx = 15
    for key in card:
        card[key] = random.sample(range(minn, maxx), 5)
        minn += 15
        maxx += 15
    return card
def showBingoCard(card):
    res = ""
    for key in card:
        res += key
        res += "\t"
    res += "\n"
    for key in range(len(card)):
        for value in card:
            res += str(card[value][key])
            res += "\t"
        res += "\n"
    print(res)

card = createBingoCard()
showBingoCard(card)
