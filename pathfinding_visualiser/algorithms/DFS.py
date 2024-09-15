import pygame

def DFS(grid, screen):


    clock = pygame.time.Clock()
    stack = []
    stack.append(grid.start_node)

    while stack:
        clock.tick(20)
        current_node = stack.pop()

        if current_node.visited is False:
            if current_node is grid.end_node:
                # if we are at end node mark as visited and reconstruct path
                current_node.visited = True
                grid.reconstruct_path(screen)
                return True
            elif current_node is grid.start_node:
                # if node is start node, mark it visited, dont change color
                current_node.visited = True
            else:
                # if node is not start or end mark as visited
                current_node.make_visited()            

            # Add neighbours of current node that haven't already been visited
            for neighbour_node in current_node.neighbours:
                if neighbour_node.visited is False:
                    stack.append(neighbour_node)
                    neighbour_node.parent_node = current_node

        grid.draw_grid(screen)

    return False


def DFS_recursive(node, grid, screen):
    clock = pygame.time.Clock()
    clock.tick(20)

    
    if node is grid.end_node:
        # found end node, mark as visited reconstruct path
        node.visited = True
        grid.reconstruct_path(screen)
        return True
    elif node is grid.start_node:
        # mark start node as visited dont change colour
        node.visited = True
    else:
        # normal node change to a visited node
        node.make_visited()
    
    grid.draw_grid(screen)

    # Search neighbour nodes that have not already been visited
    for neighbour_node in node.neighbours:
        if neighbour_node.visited is False:
            neighbour_node.parent_node = node
            found = DFS_recursive(neighbour_node, grid, screen)
            if found is True:
                return found
    
    return False

    