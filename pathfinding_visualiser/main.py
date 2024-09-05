import pygame
from .grid import Node, create_grid, draw_grid
from .utils import get_mouse_pos
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
    # Create pygame window
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
    screen.fill(BLACK)

    Node.height = WINDOW_HEIGHT // ROWS
    Node.width = WINDOW_WIDTH // COLUMNS 

    grid = create_grid(ROWS, COLUMNS)

    # Game loop
    start_node = None
    end_node = None
    running = True
    searching = False
    while running:
        draw_grid(screen, grid)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            
            if searching:
                continue
            
            # On left click assign start point, end point and walls
            if pygame.mouse.get_pressed() [0]:
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

            
            elif event.type == pygame.KEYDOWN:
                # Clear board
                if (event.key == pygame.K_c) and not searching:
                    start_node = None
                    end_node = None
                    grid = create_grid(ROWS, COLUMNS)
                
                # Start search
                elif (event.key == pygame.K_RETURN and not searching 
                    and start_node and end_node):
                    for row in grid:
                        for node in row:
                            node.set_neighbours(grid)
                    searching = True
                    BFS(start_node, end_node, grid, lambda: draw_grid(screen, grid))
                    searching = False
          

    pygame.quit()









