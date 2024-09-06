import pygame

def DFS(grid, screen):

    clock = pygame.time.Clock()
    stack = []
    stack.append(grid.start_node)

    while stack:
        clock.tick(15)
        current_node = stack.pop()

        if current_node is not grid.start_node:
            current_node.make_visited()
        else:
            current_node.visited = True
        

        if current_node is grid.end_node:
            current_node.make_end()
            grid.reconstruct_path()
            return True
        
        for neighbour_node in current_node.neighbours:
            if neighbour_node.visited is False:
                stack.append(neighbour_node)
                neighbour_node.parent_node = current_node

        grid.draw_grid(screen)
