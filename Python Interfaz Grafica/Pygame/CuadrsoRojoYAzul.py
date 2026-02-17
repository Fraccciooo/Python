import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Pygame")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Jugador
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Enemigos
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_list = [enemy_pos]
enemy_speed = 10

# Reloj
clock = pygame.time.Clock()

# Puntuación
score = 0
font = pygame.font.SysFont("Calibri", 35)

def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += enemy_speed
        else:
            enemy_list.pop(idx)
            score += 1
    return score

def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x, p_y = player_pos
    e_x, e_y = enemy_pos

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False

# Bucle principal del juego
game_over = False

def show_game_over_screen(score):
    game_over_font = pygame.font.SysFont("Calibri", 75)
    game_over_text = game_over_font.render("Game Over", True, RED)
    score_text = font.render("Score: {0}".format(score), True, WHITE)
    
    screen.fill(BLACK)
    screen.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2 - game_over_text.get_height()/2))
    screen.blit(score_text, (WIDTH/2 - score_text.get_width()/2, HEIGHT/2 + game_over_text.get_height()/2))
    
    pygame.display.update()
    pygame.time.wait(3000)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    screen.fill(BLACK)

    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)

    text = font.render("Score: {0}".format(score), True, WHITE)
    screen.blit(text, (10, 10))

    if collision_check(enemy_list, player_pos):
        game_over = True
        show_game_over_screen(score)
        break

    draw_enemies(enemy_list)
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))
    clock.tick(30)
    pygame.display.update()

pygame.quit()