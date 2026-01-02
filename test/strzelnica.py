import pygame, random  # *pygame i random do losowania pozycji celu*

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

x, y = 200, 350  # *pozycja gracza*
bullets = []  # *lista pocisków*
target_x, target_y = random.randint(50, 350), 50  # *losowa pozycja celu*

running = True

while running:
    screen.fill((0, 0, 0))  # *czyścimy ekran*

    for event in pygame.event.get():  # *sprawdzamy zdarzenia*
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append([x+15, y])  # *strzelamy pocisk z pozycji gracza*

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= 5  # *ruch w lewo*
    if keys[pygame.K_RIGHT]: x += 5  # *ruch w prawo*

    # *ruch pocisków i sprawdzanie kolizji z celem*
    for bullet in bullets[:]:
        bullet[1] -= 7  # *przesuwamy pocisk w górę*
        if bullet[1] < 0: bullets.remove(bullet)  # *usuwamy pocisk jeśli wyjdzie z ekranu*
        elif target_x < bullet[0] < target_x+30 and target_y < bullet[1] < target_y+30:
            bullets.remove(bullet)  # *usuwamy pocisk przy trafieniu*
            target_x, target_y = random.randint(50, 350), 50  # *losujemy nowy cel*

    # *rysowanie gracza i celu*
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 30, 30))  # *gracz*
    pygame.draw.rect(screen, (255, 0, 0), (target_x, target_y, 30, 30))  # *cel*
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), (*bullet, 5, 10))  # *pociski*

    pygame.display.update()
    clock.tick(60)

pygame.quit()