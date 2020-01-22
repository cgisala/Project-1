'''
2nd attempt using Card class
Integrating codes from Blackjack.py and Test3
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

    shuffledDeck = shuffle(deck) #Calls the shuffle function

    hand = deal(shuffledDeck) #Deal to dealer
    dealerHand = dealer(hand,shuffledDeck) #Dealers hand
    
    
#Takes in a deck array, shuffles it and return the array
def shuffle(array):
    random.shuffle(array)
    return array

#Pops values from the deck array and returns the popped values 
def deal(deck, hit = 2):
    if len(deck) == 0:
        return
    b = []
    for i in range(hit):
        b.append(deck.pop())
    return b

#Takes an array and calls on calc function to calculate sum the array for the dealer
def dealer(hand, deck):
    print(f'Dealer card: {hand}')
    result = calc(hand)
    return result

#Takes an array and calls on calc function to calculate sum the array for the dealer
def player(hand, deck):
    print(f'Player card: {hand}')
    result = calc(hand)
    return result

#Takes in the an array and returns an integer
def calc(array):
    num = len(array) #calculates the length of the array
    cardSum = 0
    for i in range(num):
        if array[i].rank.isdigit():  #Sums value of an array if it is numerical
            cardSum += int(array[i])
        
        #If the one of the value of an array is a King, Queen, or Jack a value of 10 is assigned
        elif array[i] == 'King' or array[i] == 'Queen' or array[i] == 'Jack':  
            cardSum += 10
        else:
            #If the value of an array is an Ace, player is given a choice to assigned a value of 1 or 11
            choice = input("Card is an ace.  Do you wan't 1 or 11: ")

            #Input Validation:  If a player inputs a letter other than number the loop repeats
            while choice.isalpha():
                print('\nError: Enter only number 1 or 11')
                choice = input("Card is an ace.  Do you wan't 1 or 11: ")
            if choice.isdigit():
                cardSum += int(choice)

    return cardSum

main()