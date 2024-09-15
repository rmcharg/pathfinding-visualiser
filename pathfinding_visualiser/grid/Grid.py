import pygame
import random
from .Node import Node



class Grid:
    """
    Class for graph implementation of grid of points
    
    Attributes:
        nodes: list
            2d list of nodes, each node labelled by row and column index
        rows: int
            number of rows in grid
        columns: int
            number of columns in grid
        start_node: Node
            node to start to search from
        end_node: Node
            target node in the search
        searching: bool
            indicate whether the graph is currently being searched for pygame loop
        target_found:
            indicate whether the end node was found
    
    """
    def __init__(self, rows, columns):
        """
        Args:
            rows: int
                number of rows in grid
            columns: int
                number of columns in grid
        """
        self.nodes = []
        self.rows = rows
        self.columns = columns
        self.start_node = None
        self.end_node = None
        self.searching = False
        self.target_found = False

    def create_grid(self, maze=False):
        """
        Create grid of nodes.

        This function initialises the grid of nodes, if the maze flag is true
        the grid is created with a random wall pattern.

        Args:
            maze: boolean
                flag to indicate whether a random maze should be generated

        """
        for i in range(self.rows):
                self.nodes.append([Node(i, j) for j in range(self.columns)])

        if maze == True:
            for row in self.nodes:
                for node in row:
                    if random.uniform(0, 1) < 0.25:
                        node.make_wall()
                    

    def get_node(self, row, column):
        """
        Returns node at given row and column in grid

        Args:
            row: int
                row position of node in grid
            column: int 
                column position of node in grid
            
        Returns:
            node at (row, column) position in grid
        """
        return self.nodes[row][column]

    def draw_grid(self, screen):
        """
        Draw grid of nodes

        Args:
            screen: pygame window object
        """
        for row in self.nodes:
            for node in row:
                node.draw(screen)

        pygame.display.flip()

    def reset_grid(self):
        """
        Function to reset the grid to state before search was performed.
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

    def reconstruct_path(self, screen):
        """
        Draw path found by search algorithm on grid
        
        Args:
            screen: pygame window object
        
        """
        node = self.end_node.parent_node

        clock = pygame.time.Clock()
        while node != self.start_node:
            clock.tick(15)
            node.make_path()
            node = node.parent_node
            self.draw_grid(screen)