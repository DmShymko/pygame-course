import pygame

#Initializnig pygame
pygame.init()

#Sets surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake")

#Set FPS and clock
FPS = 20
clock = pygame.time.Clock()

#Set game values
SNAKE_SIZE = 20

head_x = WINDOW_WIDTH//2
head_y = WINDOW_HEIGHT//2 + 100

snake_dx = 0
snake_dy = 0

score = 0

#Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
RED = (255, 0, 0)
DARK_RED = (150, 0, 0)
WHITE = (255, 255, 255)

#Set fonts
font = pygame.font.SysFont("gabriola", 48)

#Set text
title_text = font.render("~~Snake~~", True, GREEN, DARK_GREEN)
title_text_rect = title_text.get_rect()
title_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render("Score: " + str(score), True, GREEN, DARK_RED)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (10,10)
#Set sounds
#Set images

#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    #Upadae display
    pygame.display.update()

#End the game
pygame.quit()