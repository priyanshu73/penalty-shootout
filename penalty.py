import abc
import pygame
import random
import math
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800,600))

background = pygame.image.load('background.png')
pygame.display.set_caption('Penalty Shoutout')
icon = pygame.image.load('ballz.png')
pygame.display.set_icon(icon)
ballx = 375
bally = 430
ballx_change = 3
bally_change = 6
shot  = 0 
mixer.music.load('bg.wav')
mixer.music.play(-1)

#ball
ball = pygame.image.load('ball.png')
ball_state = 'ready'
def ball_fire(x,y):
    global ball_state
    ball_state = 'fire'
    screen.blit(ball,(x,y))
keeperx =360
keepery = 110
keeperx_change = 3
keepery_change = 6
#keeper 
keeper = pygame.image.load('keeper.png')
def kep_save(x,y):
    screen.blit(keeper,(x,y))
running = True 
def iscollison(a,b,c,d):
    distance = math.sqrt((math.pow(a-c,2))+(math.pow(b-d,2)))
    if distance < 50:
        return True
    else:
        return False
score_value= 0
save_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
over_font = pygame.font.Font('freesansbold.ttf',50)
overr_font = pygame.font.Font('freesansbold.ttf',32)
textx = 600
texty = 10
textxx = 10
texty = 10
#game over and scores
def show_score(x,y):
    score = font.render("SCORE: " + str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))
def show_save(x,y):
    save = font.render("SAVES: " + str(save_value),True,(255,255,255))
    screen.blit(save, (x,y))
def game_over_text():
    game_over_text = over_font.render("You Lost",True,(255,255,255))
    screen.blit(game_over_text, (300,250))
def game_win_text():
    game_win_text = over_font.render("You Won!",True,(255,255,255))
    screen.blit(game_win_text, (300,250))
def game_draw_text():
    game_draw_text = over_font.render("Tie",True,(255,255,255))
    screen.blit(game_draw_text, (300,250))

while running:
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    integers = [235,360,510]
    rand = random.randint(0,2)
    keeperr = integers[rand]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            
            keeperx = keeperr
            kep_save(keeperx,keepery)
            if event.key == pygame.K_RIGHT:
                if ball_state is 'ready':
                   shoot = mixer.Sound('shoot.wav')
                   shoot.play()
                   shoot = 'right'
                   ball_fire(ballx,bally)
            if event.key == pygame.K_LEFT:
                if ball_state is 'ready':
                   shoot = mixer.Sound('shoot.wav')
                   shoot.play()
                   shoot = 'left'
                   ball_fire(ballx,bally)
            if event.key == pygame.K_UP:
                if ball_state is 'ready':
                   shoot = mixer.Sound('shoot.wav')
                   shoot.play()
                   shoot = 'up'
                   ball_fire(ballx,bally)
    
     #collison detection and score
    collison = iscollison(keeperx,keepery,ballx,bally)   
    if collison is False and bally <= 130:
        score_value +=1
        score = mixer.Sound('laser1.wav')
        score.play()
    shot = save_value + score_value
    if collison is True  and bally<= 133:
            save_value +=1
            save = mixer.Sound('save.wav')
            save.play()
    
    
    #text display win lose draw 
    if  shot%10==0 and score_value > save_value:
        game_win_text()
        
    if shot%10==0 and save_value>score_value:
        game_over_text()
    
    tie = shot%10==0 and shot!= 0 
    
    if tie and  score_value == save_value :
        game_draw_text()
       
    #keeper reset    
    if ball_state is 'ready':
        keeperx =360
        keepery =110
    #ball reset
    if bally <= 130 :
        bally = 430
        ballx = 375
        ball_state='ready'
    #ball motion
    if ball_state is 'fire' :
        if  shoot is 'right':
            bally -= bally_change
            ballx += ballx_change
            ball_fire(ballx,bally)
        if shoot is 'left':
            bally -= bally_change
            ballx -= ballx_change
            ball_fire(ballx,bally) 
        if shoot is 'up':
            bally -= bally_change
            ball_fire(ballx,bally)
        
    screen.blit(ball,(ballx,bally))
    screen.blit(keeper,(keeperx,keepery))
    show_score(textx,texty)
    show_save(textxx,texty)
    pygame.display.update()