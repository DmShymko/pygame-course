import pygame, random  # *importujemy pygame do tworzenia gier i random do losowania pozycji jedzenia*

pygame.init()  # *uruchamiamy wszystkie moduły pygame*

screen = pygame.display.set_mode((800, 800))  # *ustawiamy okno gry o wymiarach 400x400 pikseli*
clock = pygame.time.Clock()  # *zegarek do kontrolowania prędkości gry*

x, y = 200, 200  # *początkowa pozycja węża*
dx, dy = 20, 0  # *początkowy kierunek ruchu węża (dx - zmiana X, dy - zmiana Y)*

snake = [(x, y)]  # *lista przechowująca segmenty węża*
food = (random.randrange(0, 20)*20, random.randrange(0, 20)*20)  # *losujemy pozycję jedzenia*

running = True  # *zmienna sterująca główną pętlą gry*

while running:
    pygame.time.delay(100)  # *opóźnienie między krokami gry (100 ms)*

    for event in pygame.event.get():  # *sprawdzamy wszystkie zdarzenia (klawisze, zamknięcie okna)*
        if event.type == pygame.QUIT:  # *jeśli kliknięto "X" w oknie, zakończ grę*
            running = False
        if event.type == pygame.KEYDOWN:  # *jeśli naciśnięto klawisz*
            if event.key == pygame.K_LEFT: dx, dy = -20, 0  # *ruch w lewo*
            if event.key == pygame.K_RIGHT: dx, dy = 20, 0  # *ruch w prawo*
            if event.key == pygame.K_UP: dx, dy = 0, -20  # *ruch w górę*
            if event.key == pygame.K_DOWN: dx, dy = 0, 20  # *ruch w dół*

    x += dx  # *przesuwamy węża w poziomie*
    y += dy  # *przesuwamy węża w pionie*
    snake.append((x, y))  # *dodajemy nową pozycję głowy do listy segmentów*

    if (x, y) == food:  # *sprawdzamy, czy wąż zjadł jedzenie*
        food = (random.randrange(0, 20)*20, random.randrange(0, 20)*20)  # *losujemy nowe jedzenie*
    else:
        snake.pop(0)  # *jeśli nie zjadł, usuwamy ostatni segment, żeby wąż się nie wydłużał*

    screen.fill((0, 0, 0))  # *czyścimy ekran na czarno*

    for block in snake:  # *rysujemy wszystkie segmenty węża*
        pygame.draw.rect(screen, (0, 255, 0), (*block, 20, 20))  # *zielony kwadrat 20x20*

    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))  # *czerwony kwadrat – jedzenie*

    pygame.display.update()  # *odświeżamy ekran*
    clock.tick(3)  # *ustalamy liczbę klatek na sekundę (3 FPS)*

pygame.quit()  # *kończymy działanie pygame*