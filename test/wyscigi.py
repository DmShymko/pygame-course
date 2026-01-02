import pygame, random  # *pygame i random do losowania przeszkód*

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

car_x, car_y = 180, 300  # *pozycja samochodu*
obstacles = [[random.randint(0, 350), -50]]  # *lista przeszkód (x, y)*

running = True

while running:
    screen.fill((0, 0, 0))  # *czyścimy ekran*

    for event in pygame.event.get():  # *sprawdzamy zdarzenia*
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: car_x -= 5  # *ruch w lewo*
    if keys[pygame.K_RIGHT]: car_x += 5  # *ruch w prawo*

    # *ruch przeszkód*
    for obs in obstacles[:]:
        obs[1] += 5  # *przesuwamy przeszkodę w dół*
        if obs[1] > 400:
            obs[1] = -50
            obs[0] = random.randint(0, 350)  # *losujemy nową pozycję przeszkody*

        # *sprawdzamy kolizję samochodu z przeszkodą*
        if car_x < obs[0]+50 and car_x+50 > obs[0] and car_y < obs[1]+50 and car_y+50 > obs[1]:
            print("KOLIZJA! Koniec gry")
            running = False

        pygame.draw.rect(screen, (255, 0, 0), (*obs, 50, 50))  # *rysujemy przeszkodę*

    pygame.draw.rect(screen, (0, 255, 0), (car_x, car_y, 50, 50))  # *rysujemy samochód*

    pygame.display.update()
    clock.tick(40)

pygame.quit()