import random
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Welcome to Text-based Blackjack")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
coins = 1500
print("Instructions:")
print("You have " + str(coins) + " coins.\nEach round costs 100 coins.\nEach raise is 100 coins. \nSelecting double will double your current bet.\n")
print("You can select the options by typing in the corresponding number when prompted.\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
start = input("Are you ready to begin?\n1. Yes\n2. No, end game.\nEnter number here: ")
playAgain = False
if start == "1":
    print("Let's begin!")
    playAgain = True

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

while playAgain:  
    reShuffle()
    playerTotal = points(playerHand)
    dealerTotal = points(dealerHand)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if (len(playerHand) == 2 and playerTotal == 21):
        print("BlackJack! You win!\n")
    else:
        print("You have a " + str(playerHand) + ".")
        print("You have " + str(playerTotal) + " points.\n")
        print("Dealer has a '" + str(dealerHand[0]) + "' showing.\n")
    answer = ""
    while (playerTotal) < 21 and answer != "2":
        answer = input("What would you like to do?\n1. Hit\n2. Stay\nEnter number here: ")
        if answer == "1":
            hitMe(playerHand)
            playerTotal = points(playerHand)
            print("\nYou have a " + str(playerHand) + ".")
            print("You have " + str(playerTotal) + " points.\n")
            if playerTotal > 21:
                print("\nBUST! Dealer wins!")
        elif answer == "2":
            print("\nDealer has " + str(dealerHand) + ".")
            if dealerTotal >= playerTotal:
                print("Dealer wins!")
            else:
                while dealerTotal <= 17 or dealerTotal <= playerTotal:
                    print("\nDealer takes a hit.")
                    hitMe(dealerHand)
                    dealerTotal = points(dealerHand)
                    print("Dealer has " + str(dealerHand) + ".")
                    print("Dealer has " + str(dealerTotal) + " points.")
                    if dealerTotal > 21:
                        print("\nDealer BUSTS! You win!")
                    elif dealerTotal <= 21 and dealerTotal > playerTotal:
                        print("\nDealer wins!")
    answer = input("\nWould you like to play again?\n1. Yes, play again.\n2. No, end game.\nEnter number here: ")
    if answer == "2":
        playAgain = False
        print("\nThanks for playing!")