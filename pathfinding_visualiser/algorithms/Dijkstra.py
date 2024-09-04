

def Dijkstra(start_node, end_node, grid):
    print('Running Dijkstras algo')

    # Initialise queue and append start node
    queue = []
    queue.append(start_node)

    # Initialise distances dictionary for each node
    distances = {node.index(): 0 if node == start_node else float('inf') 
                 for row in grid for node in row}
    
    while queue:
        current_node = queue.pop(0)
        current_node.visited = True
        
    
    print(distances[(1, 1)])