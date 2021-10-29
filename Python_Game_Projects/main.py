import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 700))

# add image to background of game
background = pygame.image.load('Stars.jpg')

#Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# '''Title and Icon and How to add new Icon and Title to Pycharm Game'''
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('shuttle.png')
pygame.display.set_icon(icon)

# Adding Icon or Player into your game
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 580
playerX_change = 0  # this variable is created to help with moving the icon or image on the screen

# Adding Enemy Icon
enemyImg = []
enemyX =[]
enemyY= []
enemyX_change = []
enemyY_change = []
num_of_enemies = 40

for i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.6)  # this variable is created to help with moving the icon or image on the screen on the x axis
    enemyY_change.append(40)  # this variable is created to help with moving the icon or image on the screen on the y axis

# Adding Laser Icon

# Ready state- means you can't see the bullet on the screen
# Fire state- means the bullet is currently moving
laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 580
laserX_change = 0  # this variable is created to help with moving the icon or image on the screen on the x axis
laserY_change = 10  # this variable is created to help with moving the icon or image on the screen on the y axis
laser_state = "ready"

#score variable
score_value = 0
font = pygame.font.Font('freesansbold.ttf',40)

textX = 10
textY = 10
#Game Over Txt
over_font = pygame.font.Font('freesansbold.ttf',64)
def showscore(x,y):
    score = font.render("Score :" +str(score_value),True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200,250))

# Player method to add the icon or player to the screen.
def player(x, y):
    # screen.blit means to draw which practically means you are drawing your image onto the screen
    screen.blit(playerImg, (x, y))


# Enemy method to add the icon or enemy to the screen.
def enemy(x, y, i):
    # screen.blit means to draw which practically means you are drawing your image onto the screen
    screen.blit(enemyImg[i], (x, y))


# Enemy method to add the icon or enemy to the screen.
def fire_laser(x, y):
    # screen.blit means to draw which practically means you are drawing your image onto the screen
    global laser_state
    laser_state = "fire"
    screen.blit(laserImg, (x + 1, y + 5))
    screen.blit(laserImg, (x + 35, y + 5))

#Collision method for when the laser collides with the enemy
def isCollision(enemyX, enemyY, laserX, laserY):
    #formula for distance between two points...look it up on google
    distance = math.sqrt(((math.pow(enemyX[i] - laserX, 2))) + (math.pow(enemyY[i] - laserY, 2)))
    if distance < 27: #by trial and error this become collison number
        return True
    else:
        return False


# Game Loop makes sure the game is running always and work within while loop.
running = True
while running:
    # RGB - Red, Green, Blue to change the background color of your screen
    screen.fill((21, 14, 86))

    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            # playerX_change is used to describe how much the image will be incremented by in the display
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            # used to access what the space bar function is going to do which is fire lasers
            if event.key == pygame.K_SPACE:
                # Get the current x coordinate of the spaceship
                if laser_state is "ready":
                    laser_Sound = mixer.Sound('laser.wav')
                    laser_Sound.play()
                    laserX = playerX
                    fire_laser(laserX, laserY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1
    # checking for Boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    # this allows the image not to move pass the screen size
    if (playerX <= 0):
        playerX = 0
    elif (playerX >= 736):
        playerX = 736
    # Enemy Movement
    for i in range(num_of_enemies):

        #Game over
        if enemyY[i] > 540:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        # this allows the image not to move pass the screen size
        if (enemyX[i] <= 0):
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif (enemyX[i] >= 736):
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX, enemyY, laserX, laserY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            laserY = 580
            laser_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Laser Movement
    if laserY <= 0:
        laserY = 580
        laser_state = "ready"
    if laser_state is "fire":
        fire_laser(laserX, laserY)
        laserY -= laserY_change



    player(playerX, playerY)
    showscore(textX,textY)
    pygame.display.update()
