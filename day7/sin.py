import pygame
import math

def f(x):
    return math.sin(x)  # y = sin(x)

w = 800
h = 600
pygame.init()
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Graph")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.fill((255, 255, 255))
    prev_x = -6
    prev_y = f(prev_x)
   
    h_max = 12

    for i in range(w):
        x = -6 + 12 * i/w
        y = f(x)
        pygame.draw.line(screen, (0, 0, 0),
                        (w//2 + prev_x * w/h_max,h//2 - prev_y * h/h_max),
                        (w//2 + x * w/h_max,h//2 - y * h/h_max),
                        2)
        prev_x = x
        prev_y = y


    pygame.display.flip()