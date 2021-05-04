import random

#Card list:
cards = {
    "A": {
        "Count": 4,
        "Points": 1
    },
    "2": {
        "Count": 4,
        "Points": 2
    },
    "3": {
        "Count": 4,
        "Points": 3
    },
    "4": {
        "Count": 4,
        "Points": 4
    },
    "5": {
        "Count": 4,
        "Points": 5
    },
    "6": {
        "Count": 4,
        "Points": 6
    },
    "7": {
        "Count": 4,
        "Points": 7
    },
    "8": {
        "Count": 4,
        "Points": 8
    },
    "9": {
        "Count": 4,
        "Points": 9
    },
    "10": {
        "Count": 4,
        "Points": 10
    },
    "J": {
        "Count": 4,
        "Points": 10
    },
    "Q": {
        "Count": 4,
        "Points": 10
    },
    "K": {
        "Count": 4,
        "Points": 10
    }
}
for k in cards:
    print(k, cards[k])