import pygame
import random
import math
from pygame import mixer 



pygame.init()

sound_enabled = True
try:
    pygame.mixer.init()
    mixer.music.load("background.wav")
    mixer.music.play(-1)
except pygame.error:
    print("No audio device found — running without sound.")
    sound_enabled = False

# Set up the display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Background
background = pygame.image.load("background.jpg")


# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Invader
invaderImg = []
invaderX = []
invaderY = []
invaderX_change = []
invaderY_change =[]
num_of_invaders = 6

for i in range(num_of_invaders):
    invaderImg.append(pygame.image.load('invader1.png'))
    invaderX.append(random.randint(0, 736)) 
    invaderY.append(random.randint(50, 150)) 
    invaderX_change.append(0.2)
    invaderY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0 
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"  

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10 

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))    

def player(x, y):
    screen.blit(playerImg, (x, y))

def invader(x, y, i):
    screen.blit(invaderImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10)) # Align bullet with player

def isCollision(invaderX, invaderY, bulletX, bulletY):
    distance = math.sqrt(math.pow(invaderX - bulletX, 2) + math.pow(invaderY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0,))
    # Draw background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    if sound_enabled:
                        bullet_sound = mixer.Sound("laser.wav")
                        bullet_sound.play()
                        bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Spaceship boundaries logic
    playerX += playerX_change 
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 800 - player widt (64)
        playerX = 736
    # Invader movement 
    for i in range(num_of_invaders):
        if invaderY[i] > 200:
            for j in range(num_of_invaders):
                invaderY[j] = 2000
            game_over_text()
            break
        invaderX[i] += invaderX_change[i]
        if invaderX[i] <= 0:
            invaderX_change[i] = 0.2
            invaderY[i] += invaderY_change[i]
        elif invaderX[i] >= 736:  # 800 - player widt (64)
            invaderX_change[i] = -0.2        
            invaderY[i] += invaderY_change[i]
        # Collision
        collision = isCollision(invaderX[i], invaderY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            invaderX[i] = random.randint(0, 736) 
            invaderY[i] = random.randint(50, 150)
        invader(invaderX[i], invaderY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX, textY)    
    pygame.display.update()       

    