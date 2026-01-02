import pygame, random  # *pygame do gry, random do losowania bonusów*

pygame.init()  # *uruchamiamy pygame*

screen = pygame.display.set_mode((800, 800))  # *tworzymy okno gry*
clock = pygame.time.Clock()  # *zegarek do kontroli czasu*

# pozycja gracza
player_x, player_y = 200, 200
speed = 5  # *prędkość gracza*

# pozycja bonusu
bonus_x = random.randint(20, 360)
bonus_y = random.randint(20, 360)

score = 0  # *liczba punktów*

time_limit = 30  # *czas gry w sekundach*
start_time = pygame.time.get_ticks()  # *czas startu gry*

font = pygame.font.SysFont(None, 32)  # *czcionka do tekstu*

running = True
game_over = False

while running:
    screen.fill((0, 0, 0))  # *czyścimy ekran*

    for event in pygame.event.get():  # *obsługa zdarzeń*
        if event.type == pygame.QUIT:
            running = False

    if not game_over:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player_x -= speed  # *ruch w lewo*
        if keys[pygame.K_RIGHT]: player_x += speed  # *ruch w prawo*
        if keys[pygame.K_UP]: player_y -= speed  # *ruch w górę*
        if keys[pygame.K_DOWN]: player_y += speed  # *ruch w dół*

        # *tworzymy prostokąty do kolizji*
        player_rect = pygame.Rect(player_x, player_y, 30, 30)
        bonus_rect = pygame.Rect(bonus_x, bonus_y, 20, 20)

        # *sprawdzamy, czy gracz zebrał bonus*
        if player_rect.colliderect(bonus_rect):
            score += 1  # *dodajemy punkt*
            bonus_x = random.randint(20, 360)  # *losujemy nową pozycję bonusu*
            bonus_y = random.randint(20, 360)

        # *liczymy ile czasu minęło*
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
        remaining_time = time_limit - elapsed_time

        if remaining_time <= 0:
            game_over = True  # *koniec gry po upływie czasu*

        # *rysujemy gracza i bonus*
        pygame.draw.rect(screen, (0, 255, 0), player_rect)  # *gracz*
        pygame.draw.rect(screen, (0, 0, 255), bonus_rect)  # *bonus*

        # *wyświetlamy punkty i czas*
        score_text = font.render(f"Punkty: {score}", True, (255, 255, 255))
        time_text = font.render(f"Czas: {remaining_time}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 40))

    else:
        # *ekran końcowy*
        end_text = font.render(f"Koniec gry! Punkty: {score}", True, (255, 255, 0))
        screen.blit(end_text, (80, 180))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
