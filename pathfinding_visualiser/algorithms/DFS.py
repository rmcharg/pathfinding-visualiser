import pygame

def DFS(grid, screen):

    visited = []
    clock = pygame.time.Clock()
    stack = []
    stack.append(grid.start_node)

    while stack:
        clock.tick(20)
        current_node = stack.pop()
        visited.append(current_node.index())
        if current_node.visited is True:
            current_node.colour = (210, 175, 255)

        if current_node is not grid.start_node:
            current_node.make_visited()
        else:
            current_node.visited = True
        

        if current_node is grid.end_node:
            print(visited)
            grid.reconstruct_path()
            return True
        
        for neighbour_node in current_node.neighbours:
            if neighbour_node.visited is False:
                stack.append(neighbour_node)
                neighbour_node.parent_node = current_node

        grid.draw_grid(screen)
