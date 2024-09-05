import pygame
from .Node import Node



class Grid:
    def __init__(self, rows, columns):
        self.nodes = []
        self.rows = rows
        self.columns = columns
        self.start_node = None
        self.end_node = None
        self.searching = False
        self.target_found = False

    def create_grid(self, maze=False):
        """Create grid of nodes with the number of rows and cols.
            If maze argument is passed it generates a grid with random
            walls placed.
        """
        if maze == False:
            for i in range(self.rows):
                self.nodes.append([Node(i, j) for j in range(self.columns)])

    def get_node(self, row, column):
        return self.nodes[row][column]

    def draw_grid(self, screen):
        """Draw grid of nodes
        Args:
            screen: pygame window object
        """
        for row in self.nodes:
            for node in row:
                node.draw(screen)

        pygame.display.flip()

    def reset_grid():
        pass

    def clear_grid():
        pass

    def reconstruct_path(grid):
        node = grid.end_node.parent_node

        while node != grid.start_node:
            node.make_path()
            node = node.parent_node


        


                                                                               

def create_grid(rows, columns):
    """
    Create grid of nodes with specified rows and columns
    
    Args:
        rows: number of rows in the grid
        columns: number of columns in the grid
    
    Returns:
        grid: 2d array of node objects
    """
    grid = []
    for i in range(rows):
        grid.append([Node(i, j) for j in range(columns)])

    return grid


def draw_grid(screen, grid):
    """
    Draw grid of nodes.
    
    Args:
        screen: pygame window to draw the grid
        grid: 2d array of nodes to draw
    """
   
    for row in grid:
        for node in row:
            node.draw(screen)
    
    pygame.display.flip()
