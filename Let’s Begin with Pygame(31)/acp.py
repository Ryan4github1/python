import pygame
import sys
pygame.init()
SCREEN_WIDTH= 500
SCREEN_LENGTH= 500
BLACK = (0,0,0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
pygame.display.set_caption("pygame ACTIVITY1")
background = pygame.image.load('house.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_LENGTH))
character = pygame.image.load('him-removebg-preview (1).png')
character = pygame.transform.scale(character, (250, 350))
font = pygame.font.Font(None, 50)
text = font.render("Hello Home", True, BLACK)
character_x = 100
character_y = 100
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    screen.blit(character, (character_x, character_y))
    screen.blit(text, (150, 60))
    pygame.display.flip()
pygame.quit()
sys.exit()