import pygame

pygame.init()

screen_width = 5000
screen_height = 6000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Screen Example")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

font = pygame.font.SysFont(None, 48)
text = font.render("Hello, Pygame!", True, BLUE)

rect_x = 100
rect_y = 150
rect_width = 200
rect_height = 100

running = True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
    screen.blit(text, (300, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
