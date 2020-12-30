import pygame
import random
from deck import*
from card import*
from button import*
from player import*
from createText import create_text, draw_score

#Initializing display
pygame.init()
win = pygame.display.set_mode((501, 501))
table = pygame.image.load('table.jpg')
win.blit(table, (0, 67))

#Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
darkred = (180, 0, 0)

#Deck/Cards
deck = deck(8)
deck.shuffle()

#Buttons
hit = button(win, red, 30, 442, 125, 50, text='HIT')
hit.draw_button(white)
stand = button(win, red, 175, 442, 125, 50, text='STAND')
stand.draw_button(white)

#Players
Player = player(win, deck, 25, 300, 'player')
dealer = player(win, deck, 25, 75, 'dealer')

#Variables:
count = 0
start = False
result = False
restart = False
test = True
 

#Main Script
run = True
while run: 
    
    #User input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        
        mouse = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed() 
        
        #Detection of keys and mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hit.interactive(mouse) and player_score <= 21 and start:
                Player.hit()
            if stand.interactive(mouse) and start:
                result = dealer.stand()
                start = False
                
        if keys[pygame.K_SPACE]:
            create_text('DEALER', win, 50, 150, 7, white) 
            Player.redraw()
            start = True
            test = False
        
    #Starts game        
    if start:
        restart = False
        if count % 2 == 0 and count <= 4:
            pygame.time.delay(400)
            Player.start_game()
        elif count <= 4:
            pygame.time.delay(400)
            dealer.start_game()
        count += 1 
    
    #Restarts game
    if restart:
        pygame.time.delay(2000)
        player_score = Player.restart_game()
        dealer_score = dealer.restart_game()
        count = 0
        start = True
        result = False
        
    #Hit button   
    if hit.interactive(mouse):
        hit.colour = darkred 
        hit.draw_button(white)
    else:
        hit.colour = red
        hit.draw_button(white)
    
    #Stand button    
    if stand.interactive(mouse):
        stand.colour = darkred 
        stand.draw_button(white)
    else:
        stand.colour = red
        stand.draw_button(white)
    
    #Score
    player_score = Player.getClosest()
    dealer_score = dealer.getClosest()
    draw_score(player_score, win, 385, 455)
    winner = player.find_winner(player_score, dealer_score)
    
    #Text(Score)
    if player_score > 21:
        create_text('BUST, DEALER WINS!', win, 30, 115, 225, white, True)
        restart = True
        start = False
    if player_score == 21 and (dealer_score != 21 and len(dealer.lst) == 2):
        create_text('BLACKJACK, YOU WIN!', win, 30, 115, 225, white, True)
        restart = True
        start = False
    elif len(Player.lst) >= 2 and result:
        create_text(winner, win, 30, 140, 240, white, True)
        restart = True
    if test:
        create_text('PRESS SPACE TO START', win, 28, 105, 240, white, True)
           
    pygame.display.update() 
pygame.quit()