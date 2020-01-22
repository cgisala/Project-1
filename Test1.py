'''
Testing the deal function 
'''
def main():
    a = ['1','2','King','Ace']
    h = 1

    print(f'A array before: {a}')

    c = (deal(a))
    print(f'C array: {c}')
    print(f'A array after: {a}')

    c = (deal(a))
    print(f'C array: {c}')
    print(f'A array after: {a}')

    c = (deal(a,1))
    print(f'C array: {c}')
    print(f'A array after: {a}')

#Pops values from the deck array and returns the popped values and what is remainder of the deck array
def deal(deck, hit = 2):
    print(f'Deck length: {len(deck)}')
    if len(deck) == 0:
        return
    b = []   
    for i in range(hit):
        b.append(deck.pop())
    return b
    

main()
