import math
import random
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 800,500
PLAYER_Y =380
ENEMY_COUNT= 6
COLLISION_DISTANCE= 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption("space invader")
pygame.display.set.icon(pygame.image.load(""))

background = pygame.image.load('background.html')
player_img = pygame.image.load('player.html')
enemy_img = pygame.image.load('enemy.png')
bulet_img = pygame.image.load('bullet.html')
font= pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
PLAYER_X = 370
PLAYER_X_CHANGE = 0
BULLET_X = 0
BULLET_Y= PLAYER_Y
bullet_state = "ready"
score = 0
enemies = [{
    "x": random.randint(0, SCREEN_WIDTH - 64),
    "y": random.randint(50, 150),
    "x_change": 2,
    "y_change": 20
} for i in range(ENEMY_COUNT)]
def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_enemy(enemy):
    screen.blit(enemy_img, (enemy["x"], enemy["y"]))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet.html, (x + 16, y + 10))

def is_collision(ex, ey, bx, by):
    return math.hypot(ex - bx, ey - by) < COLLISION_DISTANCE

def show_score():
    score_text = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def show_game_over():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))