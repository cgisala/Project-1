'''
1st attempt without using class
'''
import random

def main():    rank = ['2','3','4','5','6','7','8','9','10','King','Queen','Jack','Ace']
    suite = ['SPADES', 'CLUBS', 'HEARTS', 'DIAMONDS']

    deck = []

    deck = deck_maker(rank, suite, deck)

   # print(deck) #prints the deck
    print(deck[0])

    res = [int(i) for i in deck[0].split() if i.isdigit()] 
    print(res)

    shuffled = shuffle(deck)
    #print(shuffled) #prints a shuffled deck
    print(deck[0])

    res = [int(i) for i in deck[0].split() if i.isdigit()] 
    num = int(res) + 1
    print(res)
    print(num)

#Shuffles the array
def shuffle(array):
    random.shuffle(array)
    return array

#Makes decks
def deck_maker(ranks, suites, deck):
    for suite in suites:
        for rank in ranks:
            deck.append(f'{rank} of {suite}')
    return deck

def deal():
    pass

def hand():
    pass



def extractor():
    pass
if  __name__=="__main__":
    main()
