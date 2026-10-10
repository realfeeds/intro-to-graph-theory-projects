adj_matrix = [[0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 1, 0, 0, 0],
              [0, 1, 0, 1, 1, 1, 0, 0],
              [1, 0, 1, 0, 1, 1, 0, 0],
              [0, 1, 1, 1, 0, 1, 0, 0],
              [0, 0, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 0]]

def dijkstra(adj_matrix, explored_verteces, component_count=1):
    # Iterate through every connected vertex
    for v in explored_verteces:
        for j in range(len(adj_matrix)):
            # Found a new vertex that can be explored
            if adj_matrix[v][j] != 0 and j not in explored_verteces:
                # Marks new vertex as explored
                explored_verteces.append(j)
                print(f"{explored_verteces}; w = {component_count}")
                for a in adj_matrix[j]:
                    # Found a new unexplored vertex
                    if a != 0 and a not in explored_verteces: 
                        dijkstra(adj_matrix, explored_verteces, component_count)
                
    # If there exists an unexplored vertex in the graph after all connected verteces have been explored
    if len(explored_verteces) < len(adj_matrix):
        # Find an unexplored vertex and set as a new start point
        for n in range(len(adj_matrix)):
            if n not in explored_verteces:
                component_count += 1
                explored_verteces.append(n) 
                print(f"Found new component at vertex {n}")
                print(f"{explored_verteces}; w = {component_count}")
                dijkstra(adj_matrix, explored_verteces, component_count)

dijkstra(adj_matrix, [6])