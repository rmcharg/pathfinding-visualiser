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
        """Return row and column position in grid of node"""
        return (self.column, self.row)
    

    def draw (self, screen):
        """Draw node on screen"""
        pygame.draw.rect(screen, self.colour, (self.column * self.width, 
                         self.row * self.height, self.width - 2, self.height - 2))
       
    def make_start(self):
        """Set Node as starting node"""
        self.start = True
        self.colour = GREEN
    

    def make_wall(self):
        """Set node as wall node"""
        self.wall = True
        self.colour = BLACK
    

    def make_end(self):
        """Set node as target node"""
        self.end = True
        self.colour = TURQOISE

    def make_queued(self):
        """Show node is queued"""
        self.queued = True
        self.colour = YELLOW
    
    def make_visited(self):
        """Show node has been visited"""
        self.visited = True
        self.colour = BLUE
    
    def make_path(self):
        """Show that node is in the path between nodes"""
        self.colour = RED
    

    def reset(self):
        """reset node values to init values"""
        self.start = False
        self.wall = False
        self.end = False
        self.colour = WHITE 
        self.queued = False
        self.visited = False
        self.neighbours = []
        self.parent_node = None

    
    def set_neighbours(self, grid):
        """
        Determine the neighbors of the node in the grid
        
        Args:
            grid: 2d list of nodes
        """
        max_rows = grid.rows
        max_columns = grid.columns

        # check which neighbours we can add
        if self.row < max_rows - 1 and grid.get_node(self.row + 1, self.column).wall is False:
            self.neighbours.append(grid.get_node(self.row + 1, self.column))

        if self.row > 0 and grid.get_node(self.row - 1, self.column).wall is False:
            self.neighbours.append(grid.get_node(self.row - 1, self.column))

        if self.column < max_columns - 1 and grid.get_node(self.row, self.column + 1).wall is False:
            self.neighbours.append(grid.get_node(self.row, self.column + 1))

        if self.column > 0 and grid.get_node(self.row, self.column - 1).wall is False:
            self.neighbours.append(grid.get_node(self.row, self.column - 1))

