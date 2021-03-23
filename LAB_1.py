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

def choose_and_check(board,censored,coordinates,counter,player,bonus):
    x=0
    while x != 1:
        coor_1=input("choose a coordinate (ej.'(0,0) o (0,1)')>>")
        if len(coor_1)==5:
            c1=int(coor_1[3])
            x=1
        else:
            print("incorrectly entered coordinate")
            continue
    p1=board[c1]
    censored[c1] = p1
    print(censored)
    print(coordinates)
    y = 0
    while y != 1:
        coor_2=input("choose a coordinate (ej.'(0,0) o (0,1)>>')")
        if len(coor_2)==5:
            c2=int(coor_2[3])
            y=1
        else:
            print("incorrectly entered coordinate")
            continue
    p2=board[c2]
    censored[c2] = p2
    print(censored)
    print(coordinates)
    if p1 == p2:
        counter += 1
        player +=1
        bonus=1
        return(censored,counter,player,bonus)
    else:
        censored[c1] = "|¿?|" 
        censored[c2] = "|¿?|"
        bonus=0
        return(censored,counter,player,bonus)        
    
def interface (n):
    bonus=1
    player_1=0
    player_2=0
    counter=0
    cards = deck_of_cards(n)
    board,censored,coordinates = (board_of_MEMORICE(cards))
    print(censored)
    print(coordinates)
    while counter != n:
        bonus=1
        while bonus != 0 and counter!=n:
            print("player_1 turn")
            (censored,counter,player_1,bonus) = choose_and_check(board,censored,coordinates,counter,player_1,bonus)
            if counter == n:
                bonus = 0
        
        print(censored)
        print(coordinates)
        bonus=1
        while bonus != 0 and counter!=n:
            print("player_2 turn")
            (censored,counter,player_2,bonus) = choose_and_check(board,censored,coordinates,counter,player_2,bonus)
            if counter == n:
                bonus = 0        
        print(censored)
        print(coordinates)
    
    if player_1>player_2:
        print("congratulations player_1 you won")
    elif player_1<player_2:
        print("congratulations player_2 you won")
    else:
        print("this game ended in a draw") 
    return(0)    



n=int(input("How many pairs do you want to play?>>"))
bonus=1
interface (n)