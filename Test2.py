'''
Testing the calc function
'''
def main():
    a = ['1','2','King', 'Ace']
    b = ['2','Queen','Ace']
    r = ['2']
    c = cal(r)
    print(f'Card total: {c}')

#Takes in the hand array and returns an integer
def cal(array):
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


main()