import pygame
# import sys, os

# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)

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

game_over_text = font.render("GAME OVER", True, RED, DARK_GREEN)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to game again", True, RED, DARK_GREEN)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

#Set sounds and music
pick_up_sound = pygame.mixer.Sound('resources/sounds/pick_up_sound.wav')

#Set images(in this case, use simple rects... so just create their coordinates)
#For a rectangle ypu need (top-left x, top-left y, width, heigh)
apple_coord = (500, 500, SNAKE_SIZE, SNAKE_SIZE)
apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)

head_coord = (head_x, head_y, SNAKE_SIZE, SNAKE_SIZE)
head_rect = pygame.draw.rect(display_surface, GREEN, head_coord)

body_coords = []

#The main game loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_surface.fill(WHITE)

    #Blit HUD
    display_surface.blit(title_text, title_text_rect)
    display_surface.blit(score_text, score_text_rect)

    #Blit assets
    #Still need to do the body
    pygame.draw.rect(display_surface, GREEN, head_coord)
    pygame.draw.rect(display_surface, RED, apple_coord)

    #Upadae display
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()