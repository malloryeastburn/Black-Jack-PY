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

def points(who):
    total = 0
    for card in who:
        if card == 'A':
            total += 11
        elif card == "J" or card == "Q" or card == "K":
            total += 10
        else:
            total += int(card)
    return acesCheck(total,who.count("A"))

def reShuffle():
    cards.clear()
    for index in range(len(DECK)):
        cards.append(DECK[index])
        counts[index] = 4
    playerHand.clear()
    dealerHand.clear()
    playerTotal = 0
    dealerTotal = 0
    hitMe(playerHand)
    hitMe(dealerHand)
    hitMe(playerHand)
    hitMe(dealerHand)
    
def hitMe(who):
    card = random.randint(0,len(cards)-1)
    who.append(str(cards[card]))
    counts[card] -= 1
    if counts[card] < 0:
        cards.remove(cards[card])
        counts.remove(counts[card])
    return
playAgain = True
while playAgain:  
    reShuffle()
    playerTotal = points(playerHand)
    dealerTotal = points(dealerHand)
    print("You have a " + str(playerHand) + ".")
    print("You have " + str(playerTotal) + " points.")
    print("Dealer has a '" + str(dealerHand[0]) + "' showing.")
    answer = ""
    while (playerTotal) < 21 and answer != "s":
        answer = input("What would you like to do? (h, s): ")
        if answer == "h":
            hitMe(playerHand)
            playerTotal = points(playerHand)
            print("You have a " + str(playerHand) + ".")
            print("You have " + str(playerTotal) + " points.")
            if playerTotal > 21:
                print("BUST! Dealer wins!")
        elif answer == "s":
            print("Dealer has " + str(dealerHand) + ".")
            if dealerTotal >= playerTotal:
                print("Dealer wins!")
            else:
                while dealerTotal <= 17 or dealerTotal <= playerTotal:
                    hitMe(dealerHand)
                    dealerTotal = points(dealerHand)
                    print("Dealer has " + str(dealerHand) + ".")
                    print("Dealer has " + str(dealerTotal) + " points.")
                    if dealerTotal > 21:
                        print("Dealer BUSTS! You win!")
                    elif dealerTotal <= 21 and dealerTotal > playerTotal:
                        print("Dealer wins!")
    answer = input("Would you like to play again? y/n: ")
    if answer == "n":
        playAgain = False
        print("Thanks for playing!")