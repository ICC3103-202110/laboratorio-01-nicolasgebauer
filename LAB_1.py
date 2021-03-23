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

def choose_and_check(player):
    x=0
    y=0
    while x != 1:
        coor_1=input("choose the first coordinate (ej.'(0,0) o (0,1)')")
        if len(coor_1)==5:
            c1=int(coor_1[3])
            x=1
        else:
            print("incorrectly entered coordinate")
            continue
    while y != 1:
        coor_2=input("choose the second coordinate (ej.'(0,1)')")
        if len(coor_1)==5:
            c2=int(coor_2[3])
            y=1
        else:
            print("incorrectly entered coordinate")
            continue
    
    return(c1,c2)


"""def interface (n,cards,board,censored,coordinates):#creating the interface to de MEMORICE
    player_1 = 0
    player_2 = 0
    while player_1 != 2 or player_2 != 2:
"""



       
        

    
n = int(input("How many pairs do you want to play?"))
cards = deck_of_cards(n)
board,censored,coordinates = (board_of_MEMORICE(cards))
print(censored)
print(coordinates)
player=0
print(choose_and_check(player))