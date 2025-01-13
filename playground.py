#this is playground that i can test or experiment something

import pygame

class Circle:
    def __init__(self, radius, x, y) -> None:
        self.radius = radius
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.speed = 5
        self.dx = self.speed  
        self.dy = 3          # Change this
        
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
    
    def move(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.x += self.dx
        self.y += self.dy
        
        if self.x + self.radius >= SCREEN_WIDTH or self.x - self.radius <= 0:
            self.dx = -self.dx
            
        if self.y + self.radius >= SCREEN_HEIGHT or self.y - self.radius <= 0:
            self.dy = -self.dy
            

if __name__ == "__main__":
    pygame.init()
    
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 400
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    c = Circle(10, 50, 100)
    
    clock = pygame.time.Clock()
    
    running = True
    while running:
        c.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.fill((255, 255, 255))
        c.draw(screen)
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()