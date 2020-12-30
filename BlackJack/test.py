from deck import *
from card import *


###
a = deck()  ## creates one  unshuffled deck
b = deck(2) ## creates two unshuffled deck
a.shuffle()
b.shuffle()

z = a.getCard(0) ### retruns the very last card in the deck (at index 0)

print(len(a))## length of the deck

print(a) ## prints out the deck


print(b) ## prints the two decks
a.discardCard() ### removes the last card and throws it out
a.discardCard(5) ### removes the last 5 card and throws it out

c = a.drawCard() ### return a type card and stores it in c
d = a.drawCard()

print(c, "+", d) ## this will print the two cards that are added
print(c+d) ## this will print c + d (if  an ace is there this will give the minimum val)
print(c.__add__(d,False))## c+d (if  an ace is there this will give the max val)



 
