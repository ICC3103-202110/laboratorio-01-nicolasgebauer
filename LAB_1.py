def deck_of_cards(n):
    cards=[]
    for i in range (n):
        cards.append(i+1)
        cards.append(i+1)
    return(cards)

n=int(input("How many pairs do you want to play?"))
print(deck_of_cards(n))
