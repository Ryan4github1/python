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

background = pygame.image.load('background.png')
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')
bulet_img = pygame.image.load('bullet.png')
font= pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
PLAYER_X = 370
PLAYER_X_CHANGE = 0
BULLET_X = 0
BULLET_Y= PLAYER_Y
buller_state = "ready"
score = 0
enemies = [{
    
}]