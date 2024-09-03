import pygame
from .grid import Node

# Pre defined colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Window Config Settings
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
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

    grid = create_grid()

    # Variables to track whether start and end node have been assigned
    start_node = None
    end_node = None

    running = True
    while running:
        draw_grid(screen, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # On left click assign start point, end point and walls
            if pygame.mouse.get_pressed() [0]:
                # Get node that mouse has clicked on
                x, y = pygame.mouse.get_pos()
                row = y // Node.height
                col = x // Node.width
                print(f'Mouse pressed at ({col}, {row})')
                node = grid[row][col]
                print(node.start, node.end, node.wall)
                # Assign state to node
                if not start_node and node != end_node:
                    print('Assigning Start')
                    node.make_start()
                    start_node = node
                elif not end_node and node != start_node:
                    print('Assigning End')
                    node.make_end()
                    end_node = node
                elif node != start_node and node != end_node:
                    print('Assigning Wall')
                    node.make_wall()
                
                print(node.start, node.end, node.wall)

            # On right click reset the spot to default
            elif pygame.mouse.get_pressed()[2]:
                x, y = pygame.mouse.get_pos()
                row = y // Node.height
                col = x // Node.width
                print(f'Mouse pressed at ({col}, {row})')
                node = grid[row][col]

                if node == start_node:
                    start_node = None
                if node == end_node:
                    end_node = None
                node.reset()
                
    pygame.quit()


def create_grid():
    grid = []
    for i in range(ROWS):
        grid.append([Node(i, j) for j in range(ROWS)])

    return grid

def draw_grid(screen, grid):
    for i in range(ROWS):
        for j in range(COLUMNS):
            grid[i][j].draw(screen)



