import pygame  # *importujemy pygame do tworzenia gier*
pygame.init()  # *uruchamiamy moduły pygame*

screen = pygame.display.set_mode((400, 400))  # *tworzymy okno gry*
clock = pygame.time.Clock()  # *zegarek do kontrolowania prędkości gry*

# pozycja piłki
ball_x, ball_y = 200, 200  
ball_dx, ball_dy = 3, 3  # *prędkość piłki w poziomie i pionie*

paddle_x = 150  # *pozycja paletki w poziomie*

running = True  # *zmienna sterująca pętlą gry*

while running:
    screen.fill((0, 0, 0))  # *czyścimy ekran na czarno*

    for event in pygame.event.get():  # *sprawdzamy zdarzenia*
        if event.type == pygame.QUIT:  # *jeśli kliknięto "X", kończymy grę*
            running = False

    keys = pygame.key.get_pressed()  # *sprawdzamy naciśnięte klawisze*
    if keys[pygame.K_LEFT]: paddle_x -= 5  # *ruch paletki w lewo*
    if keys[pygame.K_RIGHT]: paddle_x += 5  # *ruch paletki w prawo*

    ball_x += ball_dx  # *przesuwamy piłkę w poziomie*
    ball_y += ball_dy  # *przesuwamy piłkę w pionie*

    # *odbicie piłki od ścian bocznych*
    if ball_x <= 0 or ball_x >= 380: ball_dx *= -1
    # *odbicie piłki od górnej ściany*
    if ball_y <= 0: ball_dy *= -1  
    # *odbicie piłki od paletki*
    if paddle_x <= ball_x <= paddle_x+100 and ball_y >= 380: ball_dy *= -1

    # *rysujemy paletkę*
    pygame.draw.rect(screen, (255, 255, 255), (paddle_x, 390, 100, 10))  
    # *rysujemy piłkę*
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 10)  

    pygame.display.update()  # *odświeżamy ekran*
    clock.tick(60)  # *60 klatek na sekundę*

pygame.quit()  # *kończymy pygame*