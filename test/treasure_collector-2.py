import pygame, random  # *pygame do gry, random do losowania bonusów*

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# pozycja gracza
player_x, player_y = 200, 200
speed = 5

# lista bonusów (kilka na ekranie)
bonus_list = [[random.randint(20, 360), random.randint(20, 360)] for _ in range(3)]

score = 0  # *punkty gracza*
level = 1  # *aktualny poziom*
lives = 3  # *życia gracza*

font = pygame.font.SysFont(None, 32)
running = True
game_over = False

while running:
    screen.fill((0, 0, 0))  # *czyścimy ekran*

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

        # *sprawdzanie kolizji z bonusami*
        for bonus in bonus_list:
            bonus_rect = pygame.Rect(bonus[0], bonus[1], 20, 20)
            if player_rect.colliderect(bonus_rect):
                score += 1  # *dodajemy punkt*
                # *losujemy nową pozycję bonusu*
                bonus[0] = random.randint(20, 360)
                bonus[1] = random.randint(20, 360)

        # *po osiągnięciu pewnej liczby punktów -> nowy poziom*
        if score >= level * 5:  # *co 5 punktów level w górę*
            level += 1
            # *dodajemy bonusów w wyższym poziomie*
            bonus_list.append([random.randint(20, 360), random.randint(20, 360)])

        # *rysujemy bonusy i gracza*
        pygame.draw.rect(screen, (0, 255, 0), player_rect)  # *gracz*
        for bonus in bonus_list:
            pygame.draw.rect(screen, (0, 0, 255), (*bonus, 20, 20))  # *bonus*

        # *wyświetlamy punkty, poziom i życia*
        score_text = font.render(f"Punkty: {score}", True, (255, 255, 255))
        level_text = font.render(f"Poziom: {level}", True, (255, 255, 0))
        lives_text = font.render(f"Życia: {lives}", True, (255, 0, 0))
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 40))
        screen.blit(lives_text, (10, 70))

        # *przykładowa prosta trudność: zwiększamy prędkość po każdym poziomie*
        speed = 5 + level - 1

        # *koniec gry po stracie wszystkich żyć*
        if lives <= 0:
            game_over = True

    else:
        # *ekran końcowy*
        over_text = font.render(f"Koniec gry! Punkty: {score}", True, (255, 255, 0))
        screen.blit(over_text, (80, 180))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
