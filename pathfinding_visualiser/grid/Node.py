import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
TURQOISE = (64, 224, 208)


class Node:
    width = 25
    height = 25

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.start = False
        self.wall = False
        self.end = False
        self.colour = WHITE 
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.parent_node = None
    
    
    def index(self):
        return (self.column, self.row)
    

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
        self.colour = TURQOISE

    def make_queued(self):
        self.queued = True
        self.colour = YELLOW
    
    def make_visited(self):
        self.visited = True
        self.colour = BLUE
    
    def make_path(self):
        self.colour = RED
    

    def reset(self):
        self.start = False
        self.wall = False
        self.end = False
        self.colour = (255, 255, 255)

    
    def set_neighbours(self, grid):
        """
        Determine the neighbors of the node in the grid
        
        Args:
            grid: 2d list of nodes
        """
        max_rows = len(grid)
        max_columns = len(grid[0])

        # check which neighbours we can add
        if self.row < max_rows - 1 and grid[self.row + 1][self.column].wall is False:
            self.neighbours.append(grid[self.row + 1][self.column])

        if self.row > 0 and grid[self.row - 1][self.column].wall is False:
            self.neighbours.append(grid[self.row - 1][self.column])

        if self.column < max_columns - 1 and grid[self.row][self.column + 1].wall is False:
            self.neighbours.append(grid[self.row][self.column + 1])

        if self.column > 0 and grid[self.row][self.column - 1].wall is False:
            self.neighbours.append(grid[self.row ][self.column - 1])

