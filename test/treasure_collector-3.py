import pygame, random, time  # *pygame do gry, random do losowania bonusów, time do mierzenia czasu power-upów*

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# pozycja gracza
player_x, player_y = 200, 200
speed = 5  # *domyślna prędkość gracza*

# lista zwykłych bonusów
bonus_list = [[random.randint(20, 360), random.randint(20, 360)] for _ in range(3)]

# power-up
powerup = [random.randint(20, 360), random.randint(20, 360)]
powerup_active = False  # *czy power-up działa*
powerup_start_time = 0
powerup_duration = 3000  # *czas działania power-up w ms (3 sekundy)*

score = 0
lives = 3
time_limit = 30  # *czas gry w sekundach*
start_time = pygame.time.get_ticks()

font = pygame.font.SysFont(None, 32)
running = True
game_over = False

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player_x -= speed
        if keys[pygame.K_RIGHT]: player_x += speed
        if keys[pygame.K_UP]: player_y -= speed
        if keys[pygame.K_DOWN]: player_y += speed

        player_rect = pygame.Rect(player_x, player_y, 30, 30)

        # kolizja z zwykłymi bonusami
        for bonus in bonus_list:
            bonus_rect = pygame.Rect(bonus[0], bonus[1], 20, 20)
            if player_rect.colliderect(bonus_rect):
                score += 1
                bonus[0] = random.randint(20, 360)
                bonus[1] = random.randint(20, 360)

        # kolizja z power-upem
        powerup_rect = pygame.Rect(powerup[0], powerup[1], 25, 25)
        if not powerup_active and player_rect.colliderect(powerup_rect):
            powerup_active = True
            powerup_start_time = pygame.time.get_ticks()
            speed += 3  # *tymczasowe przyspieszenie gracza*
            # losujemy nową pozycję power-upu
            powerup[0] = random.randint(20, 360)
            powerup[1] = random.randint(20, 360)

        # sprawdzamy czas działania power-up
        if powerup_active:
            if pygame.time.get_ticks() - powerup_start_time >= powerup_duration:
                powerup_active = False
                speed -= 3  # *koniec działania power-up*

        # rysowanie gracza i bonusów
        pygame.draw.rect(screen, (0, 255, 0), player_rect)  # gracz
        for bonus in bonus_list:
            pygame.draw.rect(screen, (0, 0, 255), (*bonus, 20, 20))  # zwykłe bonusy

        if not powerup_active:
            pygame.draw.rect(screen, (255, 255, 0), (*powerup, 25, 25))  # power-up (żółty)

        # liczenie czasu gry
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = time_limit - elapsed_time
        if remaining_time <= 0 or lives <= 0:
            game_over = True

        # wyświetlanie informacji
        score_text = font.render(f"Punkty: {score}", True, (255, 255, 255))
        time_text = font.render(f"Czas: {remaining_time}", True, (255, 255, 255))
        lives_text = font.render(f"Życia: {lives}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 40))
        screen.blit(lives_text, (10, 70))

    else:
        over_text = font.render(f"Koniec gry! Punkty: {score}", True, (255, 255, 0))
        screen.blit(over_text, (80, 180))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
