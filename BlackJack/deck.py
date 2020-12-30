from card import *
import random

values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suits = ["\u2663", "\u2660", "\u2666", "\u2665"]
class deck:

    def __init__(self, decks = 1):
        self.deck = []
        self.createDeck(decks)
    def __len__(self):
        return len(self.deck)

    def getCard(self, index):
        return self.deck[index]


    def createDeck(self,decks = 1):
        for x in range (decks):
            for suit in suits:
                for val in values:
                    self.deck.append(card(val, suit))


    def drawCard(self):
        return self.deck.pop()


    def discardCard(self, num = 1):
        
        if num > len(self.deck):
            print("This might have caused an error so I didn't go ahead with the operation: discard card method")
            return None

        for x in range (num):
            self.deck.pop()

    def reset(self, decks = 1):
        
        self.deck = []
        self.createDeck(decks)

    def shuffle(self):
        
        random.shuffle(self.deck)

    def __str__(self):
        
        toReturn = ""
        for x in self.deck:
            toReturn += x.__str__() + " "

        return toReturn
