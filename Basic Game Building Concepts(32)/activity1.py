import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen,(255,255,0),pygame.Rect(30,30,80,60))
    pygame.draw.rect(screen,(255,255,0),pygame.Rect(120,30,80,60),1)
    pygame.display.flip()