import random
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Welcome to Text-based Blackjack")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
coins = 1000
bet = 0
print("Instructions:")
print("You have " + str(coins) + " coins.\nEach round costs 100 coins.\nEach raise is 100 coins. \nSelecting double will double your current bet.\n")
print("You can select the options by typing in the corresponding number when prompted.\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
playAgain = False
start = input("Are you ready to begin?\n1. Yes\n2. No, end game.\nEnter number here: ")
while (start != "1" and start != "2"):
    print("\nThat wasn't a valid option. Let's try again. ")
    start = input("Are you ready to begin?\n1. Yes\n2. No, end game.\nEnter number here: ")
if start == "1":
    print("Let's begin!")
    playAgain = True
else:
    print("\nSee you next time!")

#Card list:
cards = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
DECK = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
counts = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
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
    bet = 100
    playerTotal = points(playerHand)
    dealerTotal = points(dealerHand)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    if (len(playerHand) == 2 and playerTotal == 21):
        print("BlackJack!\n")
    print("You have a " + str(playerHand) + ".")
    print("You have " + str(playerTotal) + " points.\n")
    print("Dealer has a '" + str(dealerHand[0]) + "' showing.\n")
    answer = ""
    while (playerTotal) <= 21 and answer != "2":
        if playerTotal == 21:
            answer = "2"
        else:
            answer = input("What would you like to do?\n1. Hit\n2. Stay\n3. Raise bet\n4. Double bet\nEnter number here: ")
        while (answer != "1" and answer != "2" and answer != "3" and answer != "4"):
            print("\nThat wasn't a valid option. Let's try again. ")
            answer = input("What would you like to do?\n1. Hit\n2. Stay\n3. Raise bet\n4. Double bet\nEnter number here: ")
        if answer == "1":
            print("\nDealer gives you a card.\n")
            hitMe(playerHand)
            playerTotal = points(playerHand)
            print("\nYou have a " + str(playerHand) + ".")
            print("You have " + str(playerTotal) + " points.\n")
            if playerTotal > 21:
                print("\nBUST! Dealer wins!")
                coins -= bet
        elif answer == "2":
            print("\nDealer has " + str(dealerHand) + ".")
            print("Dealer has " + str(dealerTotal) + " points.")
            if dealerTotal >= playerTotal:
                print("\nDealer wins!")
                coins -= bet
            else:
                while dealerTotal < 21 and dealerTotal < playerTotal:
                    print("\nDealer takes a card.\n")
                    hitMe(dealerHand)
                    dealerTotal = points(dealerHand)
                    print("Dealer has " + str(dealerHand) + ".")
                    print("Dealer has " + str(dealerTotal) + " points.")
                    if dealerTotal > 21:
                        print("\nDealer BUSTS! You win!")
                        coins += bet
                    elif dealerTotal <= 21 and dealerTotal >= playerTotal:
                        print("\nDealer wins!")
                        coins -= bet
        elif answer == "3":
            bet += 100
        elif answer == "4":
            bet *= 2
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("You have " + str(coins) + " coins.")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    answer = input("\nWould you like to play again?\n1. Yes, play again.\n2. No, end game.\nEnter number here: ")
    while (answer != "1" and answer != "2"):
        print("\nThat wasn't a valid option. Let's try again. ")
        answer = input("\nWould you like to play again?\n1. Yes, play again.\n2. No, end game.\nEnter number here: ")

    if answer == "2":
        playAgain = False
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("Thanks for playing!")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
