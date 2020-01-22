'''
Testing Blackjack2 with other functions
'''

import random

#Card class takes in the rank and suite and from the rank and suites array
class Card:
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite

    #Prints the number and suite of each card
    def __str__ (self):
        return f'{self.rank} of {self.suite}' 

def main():

    #Declares and initializes the rank and suites array
    rank = ['2','3','4','5','6','7','8','9','10','King','Queen','Jack','Ace']
    suites = ['SPADES', 'CLUBS', 'HEARTS', 'DIAMONDS']
    deck = [] #Declares deck array

    #The nested for loop puts 52 card objects in the deck array and each card object with a rank and suite 
    for suite in suites:
        for num in rank:
            card = Card(num,suite)
            deck.append(card)

    for i in range(0,52):
        print(deck[i])

    shuffledDeck = shuffle(deck) #Calls the shuffle function

    # hand = deal(shuffledDeck) #Deal to dealer
    # dealerHand = dealer(hand,shuffledDeck) #Dealers hand
    
    for i in range(0,52):
        print(shuffledDeck[i].rank)

#Shuffles the array
def shuffle(array):
    random.shuffle(array)
    return array
    
main()