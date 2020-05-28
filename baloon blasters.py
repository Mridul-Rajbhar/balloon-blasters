import pygame #importing module
import sys
import random
import math

pygame.init()

##colour
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue=(0,0,255)
#score
score = 0 
score_of_evil = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
#font = pygame.font.Font('freesansbold.ttf',32)
evil_textX = 200
evil_textY = 10

###HS_file="highscore.txt"
#background
bg=pygame.image.load("bg.png")

#making screen
screen = pygame.display.set_mode((800,600))

#naming and icon
name = pygame.display.set_caption("BALOON  BLASTERS")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#player
playerImg=pygame.image.load("gun.png")
playerX=50
playerY=300
playerY_change=0

#baloon

baloonImg=[ ]
baloonY=[ ]
baloonX=[ ]
baloonY_change=[ ]
baloonX_change=[ ]
num_of_baloons=5
for i in range(num_of_baloons):
    baloonImg.append(pygame.image.load("blue_baloon.png"))
    baloonY.append(random.randint(0,536))
    baloonX.append(random.randint(660,736))
    baloonY_change.append(-3)
    baloonX_change.append(-30)

#evil
evilImg=[ ]
evilY=[ ]
evilX=[ ]
evilY_change=[ ]
evilX_change=[ ]
num_of_evil=3
for j in range(num_of_evil):
    evilImg.append(pygame.image.load("evil.png"))
    evilY.append(random.randint(0,536))
    evilX.append(random.randint(660,736))
    evilY_change.append(-3)
    evilX_change.append(-30)

#bonus
bonusImg=pygame.image.load("bonus.png")
bonusY =random.randint(0,536)
bonusX=random.randint(660,736)
bonusY_change = -3
bonusX_change = -30


#bullet
bulletImg = pygame.image.load("bullet.png")
bulletY=0
bulletX=50
bulletX_change=10
bullet_state="ready"

#game intro
intro_font = pygame.font.Font('freesansbold.ttf',64)
def game_help():
    while True:
        screen.fill(black)
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
        help_text = intro_font.render("CONTROLS",True,blue)
        help_text1 = font.render("shoot - spacebar",True,blue)
        help_text2 = font.render("blue balloon - one point",True,blue)
        help_text3 = font.render("red balloon - five points",True,blue)
        help_text4 = font.render("if you hit 3 evil balloon you lose",True,blue)
        button(10,550,100,50,white,blue,action = "back")
        text_play(10,550,100,50,"BACK")
        screen.blit(help_text,(100,50))        
        screen.blit(help_text1,(100,150))
        screen.blit(help_text2,(100,200))
        screen.blit(help_text3,(100,250))
        screen.blit(help_text4,(100,300))
        pygame.display.update()

def game_intro():
    intro = True
    while intro:
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
        intro_text = intro_font.render("BALLOON BLASTERS",True,(0,102,0))
        screen.blit(intro_text,(45,50))
        button(350,200,100,50,red,blue,action = "play")
        button(350,300,100,50,red,blue,action = "help")
        button(350,400,100,50,red,blue,action = "exit")
        #button(275,500,250,50,red,blue,action = "high")
        text_play(350,200,100,50,"PLAY")
        #text_play(275,500,100,50,"HIGH SCORE")
        text_play(350,300,100,50,"HELP")
        text_play(350,400,100,50,"EXIT")
        pygame.display.update()

def button(buttonX,buttonY,width,height,act_colour,click_colour,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if buttonX+width>mouse[0]>buttonX and buttonY+height > mouse[1]>buttonY:
        pygame.draw.rect(screen,click_colour,(buttonX,buttonY,width,height))
        if (click[0]==1 and action !=None): 
            if action == "play":
                game_loop()
            elif action == "help":
                game_help()
            elif action == "back":
                game_intro()
            elif action == "play again":
                game_loop()
            elif action == "exit":
                pygame.quit()
                
            #elif action == "high":
            #
            #    pass
    else:
        pygame.draw.rect(screen,act_colour,(buttonX,buttonY,width,height))

def text_play(buttonX,buttonY,width,height,content):
    play_text = font.render(content,True,black)
    screen.blit(play_text,((buttonX + 10),(buttonY + 15)))

def game_over():
    while True:
        screen.fill(black)
        screen.blit(bg,(0,0))
        # global highscore
        global score
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
        over_text = intro_font.render("GAME OVER",True,(0,102,0))
        screen.blit(over_text,(200,100))
        button(300,400,225,50,red,white,action = "play again")
        text_play(300,400,225,50,"PLAY AGAIN")
        button(350,500,100,50,red,white,action = "exit")
        text_play(350,500,100,50,"QUIT")

        pygame.display.update()
def evil_score(x,y):
    global score_of_evil
    evil_val = font.render ("EVIL :" + str(score_of_evil),True,(255,0,0))
    screen.blit(evil_val,(x,y))

def  show_score(x,y):
    score_val = font.render("SCORE :" + str(score),True,(255,0,0))
    screen.blit(score_val,(x,y))
    
def bs_collision(bulletX,bulletY,bonusX,bonusY):
    bs_distance = math.sqrt((math.pow(bulletX-bonusX,2))+(math.pow(bulletY-bonusY,2)))
    if  bs_distance<32:
        return True
    else:
        return False
    
def b_collision(bulletX,bulletY,baloonX,baloonY):
    b_distance =  math.sqrt((math.pow(bulletX-baloonX,2))+(math.pow(bulletY-baloonY,2)))
    if  b_distance<32:
        return True
    else:
        return False

def bonus(x,y):
    screen.blit(bonusImg,(x,y))

def evil(x,y,j):
    screen.blit(evilImg[j],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+64,y+35))
    
def baloon(x,y,i):
    screen.blit(baloonImg[i],(x,y))    

def player(x,y):
    screen.blit(playerImg,(x,y))

def  e_collision(bulletX,bulletY,evilX,evilY):
    e_distance=math.sqrt((math.pow(bulletX-evilX,2))+(math.pow(bulletY-evilY,2)))
    if e_distance <32:
        return True
    else:
        return False

#main game loop
def game_loop():
    run = True
    global bullet_state
    global bulletX
    global playerY
    global playerX
    global bulletY
    global bonusX_change
    global bonusY_change
    global bonusX
    global bonusY
    global playerY_change
    global score
    global score_of_evil
    score_of_evil = 0
    score = 0
    while run:
        screen.fill((255,255,0))
        screen.blit(bg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()#uninitialize pygame modules
                sys.exit()#terminate
                
        #Key pressing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playerY_change = -3
                if event.key == pygame.K_DOWN:
                    playerY_change = 3
                if event.key  == pygame.K_SPACE:
                    if bullet_state== "ready":
                        bulletY=playerY
                        fire_bullet(bulletX,bulletY)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0
        #player
        playerY += playerY_change
        if playerY<=0:
            playerY=0
        if playerY > 472:
            playerY=472
        player(playerX,playerY)

        #baloon mechanics
        for i in range(num_of_baloons):
            baloonY[i] += baloonY_change[i]
            if baloonY[i]<=0:
                baloonY_change[i]=3
                baloonX[i]+=baloonX_change[i]
                if baloonX[i] <= 600:
                    baloonX_change[i]=30
                    baloonX[i]+=baloonX_change[i]
                elif baloonX[i] >= 700:
                    baloonX_change[i]=-30
                    baloonX[i]+=baloonX_change[i]
            elif baloonY[i]>536:
                baloonY_change[i]=-3
                baloonX[i]+=baloonX_change[i]
                if baloonX[i] <= 600:
                    baloonX_change[i]=30
                    baloonX[i]+=baloonX_change[i]
                elif baloonX[i] >= 700:
                    baloonX_change[i]=-30
                    baloonX[i]+=baloonX_change[i]
            #blue_baloon collision
            blue_collision=b_collision(bulletX,bulletY,baloonX[i],baloonY[i])
            if blue_collision:
                bulletX = 50
                bullet_state="ready"
                score += 1
                baloonX[i]=random.randint(660,736)
                baloonY[i]=random.randint(0,556)
            baloon(baloonX[i],baloonY[i],i)
            #evil mechanics
        for j in range(num_of_evil):
            evilY[j] += evilY_change[j]
            if evilY[j]<=0:
                evilY_change[j]=3
                evilX[j]+=evilX_change[j]
                if evilX[j] <= 600:
                    evilX_change[j]=30
                    evilX[j]+=evilX_change[j]
                elif evilX[j] >= 700:
                    evilX_change[j]=-30
                    evilX[j]+=evilX_change[j]
            elif evilY[j]>536:
                evilY_change[j]=-3
                evilX[j]+=evilX_change[j]
                if evilX[j] <= 600:
                    evilX_change[j]=30
                    evilX[j]+=evilX_change[j]
                elif evilX[j] >= 700:
                    evilX_change[j]=-30
                    evilX[j]+=evilX_change[j]

                    #evil_baloon collision
            evil_collision=e_collision(bulletX,bulletY,evilX[j],evilY[j])
            if evil_collision:
                bulletX = 50
                bullet_state="ready"
                score_of_evil +=1
                evilX[j]=random.randint(660,736)
                evilY[j]=random.randint(0,50)
                if score_of_evil == 3:
                    for k in range(num_of_baloons):
                        baloonY[i]=1000
                        bonusY=1000
                        game_over()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()#uninitialize pygame modules
                                sys.exit()#terminate
                        run = False
                        break
            evil(evilX[j],evilY[j],j)    

        #bonus mechanics
        bonusY += bonusY_change
        if bonusY<=0:
            bonusY_change=+3
            bonusX+=bonusX_change
            if bonusX <= 600:
                bonusX_change=30
                bonusX+=bonusX_change
            elif bonusX >= 700:
                bonusX_change=-30
                bonusX+=bonusX_change
        elif bonusY>536:
            bonusY_change=-3
            bonusX+=bonusX_change
            if bonusX <= 600:
                bonusX_change=30
                bonusX+=bonusX_change
            elif bonusX >= 700:
                bonusX_change=-30
                bonusX+=bonusX_change

        bonus_collision = bs_collision(bulletX,bulletY,bonusX,bonusY)
        if bonus_collision:
            bullet= 50
            bullet_state="ready"
            score+=5
            bonusX=random.randint(600,736)
            bonusY=random.randint(0,536)
        bonus(bonusX,bonusY)
        #bullet
        if bulletX == 800:
            bulletX=50
            bullet_state = "ready"
        if bullet_state=="fire":
            fire_bullet(bulletX,bulletY)
            bulletX += bulletX_change
        evil_score(evil_textX,evil_textY)
        show_score(textX,textY) 
        #show_high_Score()
        pygame.display.update()
game_intro()