import pygame
import tkinter as tk

def get_mouse_pos(node_height, node_width):
    """
    Get the grid position of the mouse click

    Args:
        node_height: the height of node on grid
        node_width: the width of node on grid
    
    Returns:
        row, col: index position of node in the grid
    """
    x, y = pygame.mouse.get_pos()
    row = y // node_height
    col = x // node_width

    return row, col


