'''
Integrating functions from Test1, Test2, and adding more functions
'''
import random

def main():
    deck = ['1','2','King','Ace','8','9','10']

    shuffledDeck = shuffle(deck) #Shuffle

    hand = deal(shuffledDeck) #Deal to dealer
    dealerHand = dealer(hand,shuffledDeck) #Dealers hand

    hand = deal(shuffledDeck) #Deal to player
    playerHand = player(hand,shuffledDeck) #Players hand

    print(f'\nPlayer: {playerHand}')
    print(f'Dealer: {dealerHand}')

    win(dealerHand, playerHand)

def dealer(hand, deck):
    print(f'Dealer card: {hand}')
    result = calc(hand)
    return result

def player(hand, deck):
    print(f'Player card: {hand}')
    result = calc(hand)
    return result


def win(dealer, player):
    if dealer > player:
        print('\nDealer wins')
    else:
        print('\nPlayer wins')

def shuffle(array):
    random.shuffle(array)
    return array

def calc(array):
    num = len(array)
    cardSum = 0
    for i in range(num):
        if array[i].isdigit():
            cardSum += int(array[i])
        elif array[i] == 'King' or array[i] == 'Queen' or array[i] == 'Jack':
            cardSum += 10
        else:
            choice = input("Card is an ace.  Do you wan't 1 or 11: ")
            while choice.isalpha():
                print('\nError: Enter only number 1 or 11')
                choice = input("Card is an ace.  Do you wan't 1 or 11: ")
            if choice.isdigit():
                cardSum += int(choice)

    return cardSum

def deal(deck, hit = 2):
    if len(deck) == 0:
        return
    b = []
    for i in range(hit):
        b.append(deck.pop())
    return b


main()