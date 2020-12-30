from card import *
from deck import *
from createText import create_text
import pygame

class player:
    
    def __init__(self, win, deck, x, y, user, lst = []):
        self.win = win
        self.deck = deck
        self.x = x
        self.y = y
        self.user = user
        self.lst = []
                   
    def get_cards(self):
        card = self.deck.drawCard()
        self.lst += [card]
        return card
        
    def get_image(self, r=True):
        if r:
            card = self.get_cards()
        else:
            card = self.lst[1]
        image = pygame.image.load(card.getImage())
        self.win.blit(image, (self.x, self.y))    
        self.x += 45
        return card
 
    def start_game(self):
        if self.user == 'player' and self.x <= 90:
            self.get_image()
        elif self.user == 'dealer' and self.x <= 25:
            self.get_image()
        elif self.user == 'dealer' and self.x > 25:
            card = self.get_cards()
            image = pygame.image.load('pics//x.png')
            self.win.blit(image, (70, self.y))
   
    def redraw(self):
        image = pygame.image.load('table.jpg')
        self.win.blit(image, (0, 67))

    def summ(self, Boo = True):
            summ = 0
            for x in self.lst:
                if Boo == False:
                    summ += x.getMaxVal()
                else:
                    summ += x.getMinVal()
            return summ
    
    def getClosest(self):
        x = self.summ(False)
        y = self.summ(True)
        if (x == 21):
            return x
        if (y == 21):
            return y
    
        if (x>21 and y<21):
            return y
        elif (y>21 and x<21):
            return x
    
        diff = []
        diff.append(x)
        diff.append(y)
        return max(diff)
    
    @staticmethod
    def find_winner(p: int, d: int):
        if p != 0 and d != 0:
            if p > d and p <= 21 or p < d and d > 21: 
                return 'YOU WIN!'
            elif p < d and d <= 21 or p > d and p > 21: 
                return 'DEALER WINS!'
            elif p == d and p <= 21:
                return 'PUSH' 
    
    def restart_game(self):
        self.redraw()
        self.lst = []
        self.x = 25
        return 0
        
    def hit(self):
        if len(self.lst) >= 2:
            card = self.get_image()
            return card
    
    def stand(self):
        if len(self.lst) >= 2: 
            self.get_image(False)
            self.dealer_play()
            return True
    
    def dealer_play(self):
        score = self.summ()
        while score <= 17:
            self.hit()
            score = self.summ()
            pygame.time.delay(500)
     
    

        
            
            