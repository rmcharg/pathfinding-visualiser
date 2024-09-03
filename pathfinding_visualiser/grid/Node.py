import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Node:
    width = 25
    height = 25

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.start = False
        self.wall = False
        self.end = False
        self.colour = (255, 255, 255) # Initialise node colour to white
    

    def draw (self, screen):
        pygame.draw.rect(screen, self.colour, (self.column * self.width, 
                         self.row * self.height, self.width - 2, self.height - 2))
        pygame.display.update()


    def make_start(self):
        self.start = True
        self.colour = GREEN
    

    def make_wall(self):
        self.wall = True
        self.colour = BLACK
    

    def make_end(self):
        self.end = True
        self.colour = RED
    
    def reset(self):
        self.start = False
        self.wall = False
        self.end = False
        self.colour = (255, 255, 255)



