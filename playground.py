#this for play or do/test something
class Circle:
    def __init__(self, radius, x, y) -> None:
        self.radius = radius
        self.x = x
        self.y = y
    
    def draw(self) -> None:
        print(f"{self.x}, {self.y}")
    
    def move(self, Flag) :
        if (self.x < SCREEN_WIDTH and self.y < SCREEN_HEIGHT) and Flag == False :
            self.x += 1
            self.y += 1
            if self.x == SCREEN_WIDTH and self.y == SCREEN_HEIGHT:
                Flag = True
                return Flag
            Flag = False
            return Flag

        elif self.x == 0 and self.y == 0:
            Flag = False
            return Flag

        
        elif (self.x > SCREEN_WIDTH and self.y > SCREEN_HEIGHT) or Flag == True:
            self.x -= 1
            self.y -= 1
            Flag = True
            return Flag 

if __name__ == "__main__":
    c = Circle(10, 100, 100)
    c.draw()
    SCREEN_WIDTH = 100
    SCREEN_HEIGHT = 100
    Flag = True
    while True:
        Flag = c.move(Flag)  
        c.draw()