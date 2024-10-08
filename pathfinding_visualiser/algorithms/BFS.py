
import pygame

def BFS(grid, screen):
    """
    Implementation of Breadth First Search Algorithm.
    
    Function will traverse grid using BFS, to try and find the target node, when it does
    get there it will reconstruct the path
    
    Args:
        start_node: starting node in search
        end_node: the target node in the search
        grid: 2d array containing all the nodes in the grid
        draw_func: function for updating the pygame window as the algo runs
    
    Returns:
        True or False to indicate if the spot was succesfully found
    """
    clock = pygame.time.Clock()
    # initialise queue with start node
    queue = []
    queue.append(grid.start_node)
    grid.start_node.queued = True

    while queue:
        clock.tick(20)
        current_node = queue.pop(0)
        if current_node is not grid.start_node:
            current_node.make_visited()
        else:
            grid.start_node.visited = True

        if current_node is grid.end_node:
            current_node.make_end()
            grid.reconstruct_path(screen)
            return True
        else:
            for neighbour_node in current_node.neighbours:
                if neighbour_node.queued is False and neighbour_node.visited is False:
                    queue.append(neighbour_node)
                    neighbour_node.make_queued()
                    neighbour_node.parent_node = current_node

        grid.draw_grid(screen)

    return False

def reconstruct_path(grid):
    node = grid.end_node.parent_node

    while node is not grid.start_node:
        node.make_path()
        node = node.parent_node
