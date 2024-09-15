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
    """
    Class for Node in graph representation of grid.
    
    Attributes:
        width: int
            width of node in pygame window
        height: int
            height of node in pygame window
        row: int
            row position of node in grid
        column: int
            column position of node in grid
        start: boolean
            indicate whether node is starting node
        end: boolean
            indicate whether node is the ending node
        wall: boolean
            indicate whether the node is a wall node
        queued: boolean
            indicate whether the node is queued.
        visited: boolean
            indicate whether the node has been visited.
        neighbours: list
            list of the node's neigbour nodes
        parent_node: Node
            node that was visited in previous step.
        colour: tuple
            tuple of integers with rgb values for node.

    Methods:
        index():
            returns the row and column position in grid of node
        draw(screen):
            draws the node on the pygame window represented by screen object
        make_start():
            changes the node to the start node
        make_wall():
            changes node to be a wall node
        make_end():
            changes node to be the ending node
        make_queued():
            marks node as queued
        make_visited():
            marks node as a visited node
        make_path():
            marks node as part of solution path
        reset():
            resets node to initialised state
        set_neighbours(grid):
            returns list of the neighbour nodes in the grid
    """
    width = 25
    height = 25

    def __init__(self, row, column):
        """
        Args:
            row : int
                row position of node in grid
            column: int
                column position of node in grid
        
        """
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
        """
        Return row and column position in grid of node.
        
        Returns:
            tuple: row and column position of node
        """
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
            grid: 2d list of nodes representing grid of points
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

