import random

#Card list:
cards = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
DECK = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
counts = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
#suits = [["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"], ["H","D","C","S"]]
playerHand = []
dealerHand = []
dealerTotal = 0
def acesCheck(total, aCount):
    while total > 21 and aCount > 0:
        total -= 10
        aCount -= 1
    return total
def points():
    total = 0
    for card in playerHand:
        if card == 'A':
            total += 11
        elif card == "J" or card == "Q" or card == "K":
            total += 10
        else:
            total += int(card)
    return acesCheck(total,playerHand.count("A"))
def reShuffle():
    cards.clear()
    for index in range(len(DECK)):
        cards.append(DECK[index])
        counts[index] = 4
    playerHand.clear()
    dealerHand.clear()
    playerTotal = 0
    dealerTotal = 0
    
def hitMe():
    card = random.randint(0,len(cards)-1)
    print(card)
    playerHand.append(str(cards[card]))
    counts[card] -= 1
    if counts[card] < 0:
        cards.remove(cards[card])
        counts.remove(counts[card])
    return
    
hitMe()
hitMe()
playerTotal = points()
print("You have a " + str(playerHand) + ".")
print("You have " + str(playerTotal) + " points.")
answer = ""
while (playerTotal) < 21 and answer != "s":
    answer = input("What would you like to do? (h, s): ")
    if answer == "h":
        hitMe()
        playerTotal = points()
        print("You have a " + str(playerHand) + ".")
        print("You have " + str(playerTotal) + " points.")
