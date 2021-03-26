import random
import numpy as np

def deck_of_cards(n):#creating the the deck of cards
    cards=[]#this is the deck of cards
    for i in range (n):
        cards.append(i+1)
        cards.append(i+1)
    return(cards)#return the deck of cards
def size_board(cards):# define the shape of the board
    if int(len(cards)) % 10 == 0:#%10
        mul=10
        (table,coordinates_1)=board_of_MEMORICE(cards,mul)
    elif int(len(cards)) % 8 == 0:#%8
        mul=8
        (table,coordinates_1)=board_of_MEMORICE(cards,mul)
    elif int(len(cards)) % 6 == 0:#%6
        mul=6
        (table,coordinates_1)=board_of_MEMORICE(cards,mul)
    elif int(len(cards)) % 4 == 0:#%4
        mul=4
        (table,coordinates_1)=board_of_MEMORICE(cards,mul)
    elif int(len(cards)) % 2 == 0:#%2
        mul=2
        (table,coordinates_1)=board_of_MEMORICE(cards,mul)
    board=[]
    for i in range (len(cards)):# creatin the board that contain the cards 
        x=len(cards)
        f=random.randint(0,x-1)
        c=cards[f]
        board.append(c)
        cards.pop(f)
    return(coordinates_1,table,board)
    

def board_of_MEMORICE(cards,mul):#creating the board that is censored
    coordinates_1=[" "]
    coordinates_2=[]
    censored=[]
    
    for i in range(len(cards)):
        censored.append("|¿?|")
    table = (np.array(censored).reshape(mul, int(len(censored)/mul)))
    for i in range(0,int(len(censored)/mul)):
        k = str(i)
        coordinates_1.append(("   "+k)) 
    print(coordinates_1)
    for i in range(0,int(mul)):
        k = str(i)
        coordinates_2.append((" "+k))     
    table = np.insert(table,0,coordinates_2, axis=1)
    
    return(table,coordinates_1)

def choose_and_check(board,table,coordinates_1,counter,player,bonus):# cheacking the coordinates and checking in the board an censored board
    x=0
    while x != 1:
        coor_1=input("choose a coordinate (ej.0,0 o 1,1)>>")
        if len(coor_1)==3 and coor_1[1]=="," :
            c1_1=int(coor_1[0])
            c1_2=int(coor_1[2])
            if c1_1+c1_2<len(board) and (c1_2+1)<len(coordinates_1):
                x=1
            else:
                print("incorrectly entered coordinate")
                continue
        elif len(coor_1)==4 and coor_1[1]==",":
            c1_1=int(coor_1[0])
            c1_2=(10*(int(coor_1[2])))+(int(coor_1[3]))
            if c1_1+c1_2<len(board) and (c1_2+1)<len(coordinates_1):
                x=1
            else:
                print("incorrectly entered coordinate")
                continue
        elif len(coor_1)==4 and coor_1[2]==",":
            c1_1=(10*(int(coor_1[0])))+(int(coor_1[1]))
            c1_2=int(coor_1[3])
            if c1_1+c1_2<len(board) and (c1_2+1)<len(coordinates_1):
                x=1
            else:
                print("incorrectly entered coordinate")
                continue
        else:
            print("incorrectly entered coordinate")
            continue
    p1=board[c1_1+c1_2]
    table[c1_1,c1_2+1] = p1
    print(coordinates_1)
    print(table)
    y = 0
    while y != 1:
        coor_2=input("choose a coordinate (ej.0,0 o 1,1)>>")
        if len(coor_2)==3 and coor_2[1]=="," :
            c2_1=int(coor_2[0])
            c2_2=int(coor_2[2])
            if c2_1+c2_2<len(board) and (c2_2+1)<len(coordinates_1):
                y=1
            else:
                print("incorrectly entered coordinate")
                continue
        elif len(coor_2)==4 and coor_2[1]==",":
            c2_1=int(coor_2[0])
            c2_2=(10*(int(coor_2[2])))+(int(coor_2[3]))
            if c2_1+c2_2<len(board) and (c2_2+1)<len(coordinates_1):
                y=1
            else:
                print("incorrectly entered coordinate")
                continue
        elif len(coor_2)==4 and coor_2[2]==",":
            c2_1=(10*(int(coor_2[0])))+(int(coor_2[1]))
            c2_2=int(coor_2[3])
            if c2_1+c2_2<len(board) and (c2_2+1)<len(coordinates_1):
                y=1
            else:
                print("incorrectly entered coordinate")
                continue
        else:
            print("incorrectly entered coordinate")
            continue
    p2=board[c2_1+c2_2]
    table[c2_1,c2_2+1] = p2
    print(coordinates_1)
    print(table)
    if p1 == p2:
        counter += 1
        player +=1
        bonus=1
        return(table,counter,player,bonus,coordinates_1)
    else:
        table[c1_1,c1_2+1] = "|¿?|" 
        table[c2_1,c2_2+1] = "|¿?|"
        bonus=0
        print("\n")
        return(table,counter,player,bonus,coordinates_1)

def interface (n): #the interface of the game MEMORICE
    bonus=1
    player_1=0
    player_2=0
    counter=0
    cards = deck_of_cards(n)
    (coordinates_1,table,board) = size_board(cards)
    print(table)
    while counter != n:
        bonus=1
        while bonus != 0 and counter!=n:
            print("player_1 turn")
            (table,counter,player_1,bonus,coordinates_1) = choose_and_check(board,table,coordinates_1,counter,player_1,bonus)
            if counter == n:
                bonus = 0
        print(coordinates_1)
        print(table)
        bonus=1
        while bonus != 0 and counter!=n:
            print("player_2 turn")
            (table,counter,player_2,bonus,coordinates_1) = choose_and_check(board,table,coordinates_1,counter,player_2,bonus)
            if counter == n:
                bonus = 0      
        print(coordinates_1)
        print(table)
    
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

