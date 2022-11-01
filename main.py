import pygame
import random

# Initialize the pygame
pygame.init()


# create the screen

screen = pygame.display.set_mode((1000, 800))
# Background
background = pygame.image.load("background.jpg")
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship1.png")
pygame.display.set_icon(icon)


#player
playerimg = pygame.image.load("fighter.png")
playerX = 470
playerY = 670
playerX_change = 0
def player(x,y):
    screen.blit(playerimg,(x,y))
    
#Enemy
enemyimg = pygame.image.load("alien.png")
enemyX = random.randint(0,970)
enemyY = random.randint(75,250)
enemyX_change = 0.5
enemyY_change = 40
def enemy(x,y):
    screen.blit(enemyimg,(x,y))
    
#Bullet
bulletimg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 670
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready" # Ready - you can't see the bullet on the screenl, Fire - The bullet is currently moving

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x+16,y+10))
    
# Window run LOOP
running = True
while running:
    
    #RGB
    screen.fill((0, 0, 0))
    #background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #if keystroke is pressed check wether its right or left
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change -= 0.65
                
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 0.65
                
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY) 
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
                

    #Checking for boundatires of spaceship so it doesn't go out of bounds             
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 930:
        playerX = 930
    
    
    
    #enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 930:
        enemyX_change = -0.3
        enemyY += enemyY_change
        
        
    # bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change
    enemy(enemyX,enemyY)
    player(playerX,playerY)
    pygame.display.update()
    
    
    
    
    
    
    
    
    

                