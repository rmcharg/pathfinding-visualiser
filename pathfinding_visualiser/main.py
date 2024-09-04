import pygame
from .grid import Node
from .algorithms import BFS

# Pre defined colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)

# Window Config Settings
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
ROWS = 25
COLUMNS = 25


def main ():
    pygame.init()
    # Create pygame window

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
    screen.fill(BLACK)

    # Set Node dimensions
    Node.height = WINDOW_HEIGHT // ROWS
    Node.width = WINDOW_WIDTH // COLUMNS 

    grid = create_grid(ROWS, COLUMNS)

    # Variables to track whether start and end node have been assigned
    start_node = None
    end_node = None

    # initialise game loop, track whether program is runnning and if algo is searching
    clock = pygame.time.Clock()
    running = True
    searching = False
    while running:
        draw_grid(screen, grid)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            # On left click assign start point, end point and walls
            if pygame.mouse.get_pressed() [0]:

                if searching:
                    continue

                # Get node that mouse has clicked on
                row, col = get_mouse_pos(Node.height, Node.width)
                node = grid[row][col]
                # Assign state to node
                if not start_node and node != end_node:
                    node.make_start()
                    start_node = node
                elif not end_node and node != start_node:
                    node.make_end()
                    end_node = node
                elif node != start_node and node != end_node:
                    node.make_wall()
            
            # On right click reset the spot to default
            elif pygame.mouse.get_pressed()[2]:
                row, col = get_mouse_pos(Node.height, Node.width)
                node = grid[row][col]

                if node == start_node:
                    start_node = None
                if node == end_node:
                    end_node = None
                node.reset()

            # when key is pressed run algorithm
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_RETURN and not searching 
                    and start_node and end_node):

                    for row in grid:
                        for node in row:
                            node.set_neighbours(grid)
                    
                    BFS(start_node, end_node, grid, lambda: draw_grid(screen, grid))

    pygame.quit()


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



