import pygame, random

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# lista piłek: [x, y, dx, dy, promień]
balls = []
for _ in range(5):
    x = random.randint(50, 350)
    y = random.randint(50, 350)
    dx = random.choice([-3, -2, 2, 3])
    dy = random.choice([-3, -2, 2, 3])
    balls.append([x, y, dx, dy, 20])  # *x, y, prędkości, promień*

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ruch i odbicie piłek od ścian
    for ball in balls:
        ball[0] += ball[2]  # *ruch w poziomie*
        ball[1] += ball[3]  # *ruch w pionie*

        # odbicie od lewej/prawej ściany
        if ball[0] <= ball[4] or ball[0] >= 400 - ball[4]:
            ball[2] *= -1
        # odbicie od góry/dół
        if ball[1] <= ball[4] or ball[1] >= 400 - ball[4]:
            ball[3] *= -1

    # odbicia między piłkami
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            dx = balls[i][0] - balls[j][0]
            dy = balls[i][1] - balls[j][1]
            distance = (dx ** 2 + dy ** 2) ** 0.5
            min_dist = balls[i][4] + balls[j][4]
            if distance < min_dist:
                # obliczamy nadmiar odległości
                overlap = min_dist - distance
                if distance == 0:
                    distance = 0.1  # *unikamy dzielenia przez 0*
                # przesuwamy piłki na zewnątrz
                balls[i][0] += (dx / distance) * (overlap / 2)
                balls[i][1] += (dy / distance) * (overlap / 2)
                balls[j][0] -= (dx / distance) * (overlap / 2)
                balls[j][1] -= (dy / distance) * (overlap / 2)

                # zmiana kierunku prędkości
                balls[i][2], balls[j][2] = -balls[i][2], -balls[j][2]
                balls[i][3], balls[j][3] = -balls[i][3], -balls[j][3]

    # rysowanie piłek
    for ball in balls:
        pygame.draw.circle(screen, (0, 255, 0), (int(ball[0]), int(ball[1])), ball[4])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
