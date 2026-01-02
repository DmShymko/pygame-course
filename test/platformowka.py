import pygame  # *importujemy pygame*

pygame.init()  # *uruchamiamy moduły pygame*

screen = pygame.display.set_mode((400, 400))  # *tworzymy okno gry*
clock = pygame.time.Clock()  # *zegarek do kontroli prędkości*

x, y = 50, 300  # *pozycja postaci*
vy = 0  # *prędkość pionowa*
on_ground = True  # *czy postać stoi na ziemi*

running = True  # *zmienna sterująca pętlą gry*

while running:
    for event in pygame.event.get():  # *sprawdzamy zdarzenia*
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # *sprawdzamy klawisze*
    if keys[pygame.K_LEFT]: x -= 5  # *ruch w lewo*
    if keys[pygame.K_RIGHT]: x += 5  # *ruch w prawo*
    if keys[pygame.K_SPACE] and on_ground: vy = -15; on_ground = False  # *skok*

    vy += 1  # *grawitacja – przyspieszenie w dół*
    y += vy  # *przesuwamy postać w pionie*
    if y >= 300: y = 300; vy = 0; on_ground = True  # *stan na ziemi*

    screen.fill((0, 0, 0))  # *czyścimy ekran*

    pygame.draw.rect(screen, (0, 255, 0), (x, y, 30, 30))  # *rysujemy postać*
    pygame.draw.rect(screen, (255, 255, 0), (0, 330, 400, 70))  # *rysujemy podłogę*

    pygame.display.update()  # *odświeżamy ekran*
    clock.tick(60)  # *60 FPS*

pygame.quit()  # *kończymy pygame*