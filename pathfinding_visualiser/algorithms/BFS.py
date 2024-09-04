

def BFS(start_node, end_node, grid, draw_func):
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
    # initialise queue with start node
    queue = []
    queue.append(start_node)
    start_node.queued = True

    while queue:
        current_node = queue.pop(0)
        if current_node != start_node:
            current_node.make_visited()

        if current_node == end_node:
            current_node.make_end()
            reconstruct_path(start_node, end_node, grid)
            return True
        else:
            for neighbour_node in current_node.neighbours:
                if neighbour_node.queued == False and neighbour_node.visited == False:
                    queue.append(neighbour_node)
                    neighbour_node.make_queued()
                    neighbour_node.parent_node = current_node

        draw_func()

    return False

def reconstruct_path(start_node, end_node, grid):
    node = end_node.parent_node

    while node != start_node:
        node.make_path()
        node = node.parent_node
