import pygame, random
from pygame import surface

#Initialize pygame
pygame.init()

#Set display surface
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = .5

score = 0
payer_lives = PLAYER_STARTING_LIVES

clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1, 1])
clown_dy = random.choice([-1, 1])

#Set colors
BLUE = (1,175,209)
YELLOW = (248,231,28)

#Set fonts
font = pygame.font.Font("resources/fonts/Franxurter.ttf", 32)

#Set text
title_text = font.render("Cath the Clown", True, BLUE)
text_rect = title_text.get_rect()
text_rect.topleft = (50,10)

score_text = font.render("Score: " + str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH - 50, 10)

lives_text = font.render("Lives: " + str(payer_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH - 50, 50)


#Set images
clown = pygame.image.load("resources/images/clown.png")
clown_rect = clown.get_rect()
clown_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

#Set sound and music

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the screen
    display_surface.fill((0,0,0))

    #Blit
    display_surface.blit(clown, clown_rect)

    #Update display
    pygame.display.update()

#End the game
pygame.quit()