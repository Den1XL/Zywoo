import pygame
H = 600
W = 800
RED == (255, 0, 0)
WHITE == (255, 255, 255)
YELLOW == (255, 255, 0)
block = 0
start = 1

pygame.init()
pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

front = pygame.font.SysFont('Arial', 32, True, False)
font2 = pygame.font.SysFont('Arial', 20, True, False)
square = pygame.Surface((60, 60))

run = True
while run:
    for e in pygame.event.get()
        if e.type == pygame.KEYDOWN:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
                
    if block == 0:
        screen.fill(BLUE)
        screen.blit(square, square_rect)
        squatr.fill(RED)
        
    pygame.display.update()