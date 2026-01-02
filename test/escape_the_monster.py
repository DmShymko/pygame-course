import pygame  # *importujemy pygame do tworzenia gry*

pygame.init()  # *uruchamiamy pygame*

screen = pygame.display.set_mode((800, 800))  # *tworzymy okno gry*
clock = pygame.time.Clock()  # *zegarek do kontroli prędkości*

# pozycja gracza
player_x, player_y = 200, 200

# pozycja przeciwnika
enemy_x, enemy_y = 50, 50

speed = 4  # *prędkość ruchu gracza*
enemy_speed = 2  # *prędkość przeciwnika*

lives = 3  # *liczba żyć gracza*

font = pygame.font.SysFont(None, 36)  # *czcionka do wyświetlania tekstu*

running = True
game_over = False  # *czy gra się skończyła*

while running:
    screen.fill((0, 0, 0))  # *czyścimy ekran*

    for event in pygame.event.get():  # *obsługa zdarzeń*
        if event.type == pygame.QUIT:
            running = False

    if not game_over:  # *jeśli gra jeszcze trwa*

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player_x -= speed  # *ruch w lewo*
        if keys[pygame.K_RIGHT]: player_x += speed  # *ruch w prawo*
        if keys[pygame.K_UP]: player_y -= speed  # *ruch w górę*
        if keys[pygame.K_DOWN]: player_y += speed  # *ruch w dół*

        # *logika pościgu – przeciwnik goni gracza*
        if enemy_x < player_x: enemy_x += enemy_speed
        if enemy_x > player_x: enemy_x -= enemy_speed
        if enemy_y < player_y: enemy_y += enemy_speed
        if enemy_y > player_y: enemy_y -= enemy_speed

        # *tworzymy prostokąty do sprawdzania kolizji*
        player_rect = pygame.Rect(player_x, player_y, 30, 30)
        enemy_rect = pygame.Rect(enemy_x, enemy_y, 30, 30)

        # *jeśli przeciwnik dotknie gracza*
        if player_rect.colliderect(enemy_rect):
            lives -= 1  # *zabieramy jedno życie*
            enemy_x, enemy_y = 50, 50  # *resetujemy pozycję przeciwnika*
            if lives <= 0:
                game_over = True  # *koniec gry*

        pygame.draw.rect(screen, (0, 255, 0), player_rect)  # *rysujemy gracza*
        pygame.draw.rect(screen, (255, 0, 0), enemy_rect)  # *rysujemy przeciwnika*

        # *wyświetlamy liczbę żyć*
        text = font.render(f"Zycia: {lives}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

    else:
        # *ekran końca gry*
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (120, 180))

    pygame.display.update()
    clock.tick(50)

pygame.quit()
