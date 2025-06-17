import pygame
import sys
pygame.init()
SCREEN_WIDTH= 500
SCREEN_LENGTH= 500
BLACK = (0,0,0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
pygame.display.set_caption("pygame ACTIVITY1")
background = pygame.image.load('download.jpg')
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_LENGTH))
character = pygame.image.load('person.jpg')
character = pygame.transform.scale(character, (100, 150))
font = pygame.font.Font(None, 50)
text = font.render("Hello world", True, BLACK)
character_x = 100
character_y = 100
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0,0))
    screen.blit(character, (character_x, character_y))
    screen.blit(text, (200, 100))
    pygame.display.flip()
pygame.quit()
sys.exit()