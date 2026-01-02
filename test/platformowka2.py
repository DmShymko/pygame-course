import pygame

pygame.init()

# okno gry
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mały Skoczek")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)

# gracz
player_x = 50
player_y = 300
player_width = 30
player_height = 40

player_speed = 5
jump_power = -12  # *siła skoku (ujemna, bo góra to mniejsze Y)*
gravity = 0.6
player_y_speed = 0
on_ground = False  # *czy gracz stoi na platformie*

# platformy
platforms = [
    pygame.Rect(0, 350, 600, 50),   # ziemia
    pygame.Rect(150, 280, 120, 20),
    pygame.Rect(330, 220, 120, 20),
    pygame.Rect(500, 160, 80, 20)
]

# punkt (cel)
goal = pygame.Rect(550, 120, 30, 30)

running = True
game_over = False
win = False

while running:
    screen.fill((135, 206, 235))  # *niebo*

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over and not win:
        # ruch w lewo / prawo
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        # skok
        if keys[pygame.K_SPACE] and on_ground:
            player_y_speed = jump_power
            on_ground = False

        # grawitacja
        player_y_speed += gravity
        player_y += player_y_speed

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        on_ground = False

        # kolizje z platformami
        for platform in platforms:
            if player_rect.colliderect(platform) and player_y_speed >= 0:
                player_y = platform.top - player_height
                player_y_speed = 0
                on_ground = True

        # sprawdzanie wygranej
        if player_rect.colliderect(goal):
            win = True

        # jeśli spadnie poza ekran
        if player_y > HEIGHT:
            game_over = True

        # rysowanie platform
        for platform in platforms:
            pygame.draw.rect(screen, (100, 100, 100), platform)

        # rysowanie celu
        pygame.draw.rect(screen, (255, 215, 0), goal)

        # rysowanie gracza
        pygame.draw.rect(screen, (0, 0, 255), player_rect)

    elif game_over:
        screen.fill((0, 0, 0))
        screen.blit(font.render("GAME OVER", True, (255, 0, 0)), (220, 160))
        screen.blit(font.render("R - restart", True, (255, 255, 255)), (240, 200))
        if keys[pygame.K_r]:
            pygame.quit()
            pygame.init()
            exec(open(__file__).read())

    elif win:
        screen.fill((0, 100, 0))
        screen.blit(font.render("WYGRAŁEŚ!", True, (255, 255, 255)), (230, 160))
        screen.blit(font.render("R - restart", True, (255, 255, 255)), (240, 200))
        if keys[pygame.K_r]:
            pygame.quit()
            pygame.init()
            exec(open(__file__).read())

    pygame.display.update()
    clock.tick(60)

pygame.quit()
