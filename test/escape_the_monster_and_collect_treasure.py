import pygame, random, os

pygame.init()

# ----------------------
# Stałe i ustawienia
# ----------------------
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Uciekaj i zbieraj")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)

# ----------------------
# Funkcje do menu
# ----------------------
def draw_text(text, x, y, color=(255,255,255)):
    # *rysujemy tekst na ekranie*
    screen.blit(font.render(text, True, color), (x, y))

def load_highscore():
    # *wczytanie najlepszego wyniku z pliku*
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            return int(f.read())
    return 0

def save_highscore(score):
    # *zapis najlepszego wyniku do pliku*
    with open("highscore.txt", "w") as f:
        f.write(str(score))

# ----------------------
# Menu startowe
# ----------------------
def main_menu():
    menu_running = True
    while menu_running:
        screen.fill((0,0,0))
        draw_text("UCIEKAJ I ZBIERAJ", 120, 100)
        draw_text("Naciśnij S aby START", 130, 160)
        draw_text("Naciśnij Q aby WYJŚCIE", 120, 200)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    menu_running = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# ----------------------
# Funkcja gry
# ----------------------
def game():
    # ustawienia gracza
    player_x, player_y = 250, 300
    speed = 5
    lives = 3
    score = 0
    time_limit = 30
    start_time = pygame.time.get_ticks()

    # przeciwnik
    enemy_x, enemy_y = random.randint(0, 470), random.randint(0, 50)
    enemy_speed = 2

    # bonus
    bonus_x, bonus_y = random.randint(20, 480), random.randint(20, 380)

    highscore = load_highscore()
    running = True
    game_over = False

    while running:
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: player_x -= speed
            if keys[pygame.K_RIGHT]: player_x += speed
            if keys[pygame.K_UP]: player_y -= speed
            if keys[pygame.K_DOWN]: player_y += speed

            # obiekty
            player_rect = pygame.Rect(player_x, player_y, 30, 30)
            enemy_rect = pygame.Rect(enemy_x, enemy_y, 30, 30)
            bonus_rect = pygame.Rect(bonus_x, bonus_y, 20, 20)

            # ruch przeciwnika
            if enemy_x < player_x: enemy_x += enemy_speed
            if enemy_x > player_x: enemy_x -= enemy_speed
            if enemy_y < player_y: enemy_y += enemy_speed
            if enemy_y > player_y: enemy_y -= enemy_speed

            # kolizje
            if player_rect.colliderect(enemy_rect):
                lives -= 1
                enemy_x, enemy_y = random.randint(0, 470), random.randint(0, 50)
                if lives <= 0:
                    game_over = True

            if player_rect.colliderect(bonus_rect):
                score += 1
                bonus_x, bonus_y = random.randint(20, 480), random.randint(20, 380)

            # liczenie czasu
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            remaining_time = time_limit - elapsed_time
            if remaining_time <= 0:
                game_over = True

            # rysowanie
            pygame.draw.rect(screen, (0,255,0), player_rect)  # gracz
            pygame.draw.rect(screen, (255,0,0), enemy_rect)   # przeciwnik
            pygame.draw.rect(screen, (0,0,255), bonus_rect)   # bonus

            # wyświetlanie informacji
            draw_text(f"Punkty: {score}", 10, 10)
            draw_text(f"Życia: {lives}", 10, 40)
            draw_text(f"Czas: {remaining_time}", 10, 70)
            draw_text(f"Najlepszy wynik: {highscore}", 10, 100)

        else:
            draw_text("GAME OVER", 180, 150, (255,0,0))
            draw_text(f"Punkty: {score}", 200, 180)
            # zapis najlepszego wyniku
            if score > highscore:
                save_highscore(score)
                draw_text("NOWY REKORD!", 170, 220, (255,255,0))
            draw_text("Naciśnij R aby ZAGRAĆ PONOWNIE", 70, 260)
            draw_text("Naciśnij Q aby WYJŚCIE", 120, 300)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return game()  # *restart gry*
            if keys[pygame.K_q]:
                pygame.quit()
                quit()

        pygame.display.update()
        clock.tick(60)

# ----------------------
# Start programu
# ----------------------
main_menu()
game()
