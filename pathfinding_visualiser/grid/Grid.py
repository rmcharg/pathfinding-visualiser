import pygame
from .Node import Node

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
