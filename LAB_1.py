import random

def deck_of_cards(n):#creating the the deck of cards
    cards=[]#this is the deck of cards
    for i in range (n):
        cards.append(i+1)
        cards.append(i+1)
    return(cards)#return the deck of cards

def board_of_MEMORICE(cards):#creating the board
    board=[]#this is the board
    censored=[]#this is the censored board
    coordinates=[]#this are the coordinates of de censored blocks
    for i in range (len(cards)):
        x=len(cards)
        f=random.randint(0,x-1)
        c=cards[f]
        board.append(c)
        censored.append(" |¿?|")
        coordinates.append("(0,"+str(i)+")")
        cards.pop(f)
    return(board,censored,coordinates)


       
        

    
n = int(input("How many pairs do you want to play?"))
cards = deck_of_cards(n)
board,censored,coordinates = (board_of_MEMORICE(cards))
print(censored)
print(coordinates)