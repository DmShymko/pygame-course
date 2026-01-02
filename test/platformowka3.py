import pygame, random

pygame.init()

WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Przygoda Małego Bohatera")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

# --- gracz ---
player = pygame.Rect(50, 300, 30, 40)
player_speed = 5
jump_power = -12
gravity = 0.6
y_speed = 0
on_ground = False
lives = 3
score = 0

# --- poziomy ---
levels = [
    {
        "platforms": [
            pygame.Rect(0, 350, 700, 50),
            pygame.Rect(150, 280, 120, 20),
            pygame.Rect(350, 230, 120, 20)
        ],
        "enemy": pygame.Rect(400, 320, 30, 30),
        "goal": pygame.Rect(650, 320, 30, 30),
        "bonus": pygame.Rect(200, 250, 20, 20)
    },
    {
        "platforms": [
            pygame.Rect(0, 350, 700, 50),
            pygame.Rect(100, 300, 120, 20),
            pygame.Rect(300, 240, 120, 20),
            pygame.Rect(500, 180, 120, 20)
        ],
        "enemy": pygame.Rect(300, 320, 30, 30),
        "goal": pygame.Rect(620, 140, 30, 30),
        "bonus": pygame.Rect(520, 150, 20, 20)
    }
]

level_index = 0

running = True
game_over = False
win = False

while running:
    screen.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not game_over and not win:

        # --- ruch gracza ---
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        if keys[pygame.K_SPACE] and on_ground:
            y_speed = jump_power
            on_ground = False

        # --- grawitacja ---
        y_speed += gravity
        player.y += y_speed
        on_ground = False

        # --- platformy ---
        for p in levels[level_index]["platforms"]:
            if player.colliderect(p) and y_speed >= 0:
                player.bottom = p.top
                y_speed = 0
                on_ground = True

        # --- przeciwnik ---
        enemy = levels[level_index]["enemy"]
        if enemy.x < player.x:
            enemy.x += 2
        else:
            enemy.x -= 2

        if player.colliderect(enemy):
            lives -= 1
            player.x, player.y = 50, 300
            if lives <= 0:
                game_over = True

        # --- bonus ---
        bonus = levels[level_index]["bonus"]
        if bonus and player.colliderect(bonus):
            score += 1
            levels[level_index]["bonus"] = None

        # --- cel ---
        if player.colliderect(levels[level_index]["goal"]):
            level_index += 1
            player.x, player.y = 50, 300
            if level_index >= len(levels):
                win = True

        # --- rysowanie ---
        for p in levels[level_index]["platforms"]:
            pygame.draw.rect(screen, (100, 100, 100), p)

        pygame.draw.rect(screen, (0, 0, 255), player)
        pygame.draw.rect(screen, (255, 0, 0), enemy)
        pygame.draw.rect(screen, (255, 215, 0), levels[level_index]["goal"])
        if bonus:
            pygame.draw.rect(screen, (0, 255, 0), bonus)

        screen.blit(font.render(f"Życia: {lives}", True, (0,0,0)), (10,10))
        screen.blit(font.render(f"Punkty: {score}", True, (0,0,0)), (10,40))

    elif game_over:
        screen.fill((0,0,0))
        screen.blit(font.render("GAME OVER", True, (255,0,0)), (300,180))

    elif win:
        screen.fill((0,150,0))
        screen.blit(font.render("WYGRAŁEŚ CAŁĄ GRĘ!", True, (255,255,255)), (230,180))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
