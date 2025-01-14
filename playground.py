#this is playground that i can test or experiment something

import pygame
from random import randint
class Circle:
    def __init__(self, radius, x, y, speed, dy, color) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed
        self.dx = self.speed  
        self.dy = dy     
        
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT, set):
        self.x += self.dx
        self.y += self.dy
        
        if self.x >= SCREEN_WIDTH or self.x  < 0:    #self.x must > self.radius
            self.dx = -self.dx
            
        if self.y >= SCREEN_HEIGHT or self.y < 0:
            self.dy = -self.dy

        for i in set:
            if i != self:
                if (self.x - i.x)**2 + (self.y - i.y)**2 <= (self.radius + i.radius)**2:
                    self.dx = -self.dx
                    self.dy = -self.dy
                    i.dx = -i.dx
                    i.dy = -i.dy
        
        
            

if __name__ == "__main__":
    pygame.init()
    
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    number_of_circle = int(input())
    circle_group = []
    for i in range(number_of_circle):
        r = randint(10,50)
        c = Circle(
            r,
            randint(r+1,SCREEN_WIDTH - 1),
            randint(r+1,SCREEN_HEIGHT - 1),
            randint(1,5),
            randint(1,10),
            (randint(0,255),randint(0,255),randint(0,255))
        )
        circle_group.append(c)
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((255, 255, 255))
        
        for x in circle_group:
            x.move(SCREEN_WIDTH, SCREEN_HEIGHT, circle_group)
            x.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()