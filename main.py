import pygame
import random
import math


pygame.init()
screen=pygame.display.set_mode((800,600))
background=pygame.image.load('background.jpg')

pygame.display.set_caption("Space Invaders")
icon=pygame.image.load('red.png')
pygame.display.set_icon(icon)

playerimg=pygame.image.load('player.png')
playerx=370
playery=480
playerx_change=0

enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies=6

bulletimg=pygame.image.load('bullet.png')
bulletx=0
bullety=480
bulletx_change=0
bullety_change=20
bullet_state='ready'

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemy.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(0,150))
    enemyx_change.append(5)
    enemyy_change.append(40)

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
game_font=pygame.font.Font('freesansbold.ttf',64)

restart_font=pygame.font.Font('freesansbold.ttf',40)

def show_score(x,y):
    score=font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    gover=game_font.render("GAME OVER",True,(255,255,255))
    screen.blit(gover,(200,250))


    
    

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    for i in range(num_of_enemies):
        screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))
    
def iscollition(enemyx,enemyy,bulletx,bullety):

    dis=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))

    if dis<27:
        return True
    else:
        return False


running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerx_change=-5
            if event.key==pygame.K_RIGHT:
                playerx_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bulletx=playerx
                    fire_bullet(bulletx,bullety)
            

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerx_change=0
    
            
            
        
    
    playerx+=playerx_change
    if playerx<=0:
        playerx=0
        
    elif playerx>=736:
        playerx=736
    for i in range(num_of_enemies):

        if enemyy[i]>=400:
            for j in range(num_of_enemies):
                enemyy[j]=2000
            game_over_text()
                
            break
        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=4
            enemyy[i]+=enemyy_change[i]

        elif enemyx[i]>=736:
            enemyx_change[i]=-4
            enemyy[i]+=enemyy_change[i]

    
        collition=iscollition(enemyx[i],enemyy[i],bulletx,bullety)

        if collition:
            bullety=480
            bullet_state="ready"
            score_value+=1
            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(0,150)

        enemy(enemyx[i],enemyy[i])

    if bullety<=0:
        bullety=480
        bullet_state="ready"

    if bullet_state=="fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
        
        
                      
    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()

















    
