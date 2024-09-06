import pygame
import random
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
        for i in range(self.rows):
                self.nodes.append([Node(i, j) for j in range(self.columns)])
        if maze == True:
            for row in self.nodes:
                for node in row:
                    if random.uniform(0, 1) < 0.25:
                        node.make_wall()
                    

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

    def reset_grid(self):
        """
        Function to reset the grid to state before algorithm was run this 
        will allow algorithm to be run on the same grid wall format
        """
        self.start_node.queued = False
        self.start_node.visited = False
        self.end_node.visited = False
        self.end_node.queued = False
        for row in self.nodes:
            for node in row:
                if (node is not self.start_node and node is not self.end_node
                    and not node.wall):
                    node.reset()

    def clear_grid():
        pass

    def reconstruct_path(grid):
        node = grid.end_node.parent_node

        while node != grid.start_node:
            node.make_path()
            node = node.parent_node