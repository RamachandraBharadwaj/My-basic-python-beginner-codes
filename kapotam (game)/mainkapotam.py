import pygame
import random 
import sys
import math
from pygame import mixer
#initialise the pygame

pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))

background = pygame.image.load('background.png')

mixer.music.load('pakshi.mp3')
mixer.music.play(-1)



pygame.display.set_caption("kapotam")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemylist
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

#enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 0

#feather
#if it's in ready state, you can't see the feather
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'


score = 0
font = pygame.font.Font('freesansbold.ttf',24)
textx= 10
texty= 10

def show_score(x,y):
    scorefin = font.render("score : " + str(score), True, (255,255,255))
    screen.blit(scorefin, (x,y))

def player(x,y):
    screen.blit(playerImg, (x,y))

def enemy (x,y):
    screen.blit(enemyImg, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+8,y+21))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
    

#game loop
running = True
while running:
    screen.fill((0,0,0))

    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

             # if keystroke is pressed check whether it's left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
               playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('bond.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
    #checking for boundaries
                
    playerX += playerX_change

    if playerX  <=0:
        playerX = 0
    elif playerX >=736:
         playerX = 736

    enemyX += enemyX_change

    if enemyX  <=0:
        enemyX_change = 4
    elif enemyX >=736:
         enemyX_change = -4


    if bulletY<=0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        
    #collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score+= 1
        enemyX = random.randint(0,736)
        enemyY = random.randint(50,150)

    player(playerX,playerY)
    show_score(textx,texty)
    enemy(enemyX,enemyY)
    pygame.display.update()
    
