from graph_using_adjacency_matrix import GraphAdjacencyMatrix
from collections import deque

def has_path(graph, start_index, end_index):
    num_vertices = graph.num_vertices
    edge_matrix = graph.adj_matrix
    # result = traverse_dfs(start_index, end_index, [], edge_matrix)
    result = traverse_bfs(start_index, end_index, [], edge_matrix)
    return result

def traverse_dfs(start_index, end_index, visited, edge_matrix, result= False):
    current_index = start_index
    if current_index == end_index:
        return True  
    visited.append(current_index)

    for neighbour in range(len(edge_matrix)):
        if edge_matrix[current_index][neighbour] > 0:
            if neighbour not in visited:
                result = traverse_dfs(neighbour, end_index, visited, edge_matrix)
                if result:
                    break
    
    return result

def traverse_bfs(start_index, end_index, visited, edge_matrix):
    queue = deque()
    queue.append(start_index)
    visited.append(start_index)

    while len(queue) != 0:
        current_index = queue.popleft()
        if current_index == end_index:
            return True

        for neighbour in range(len(edge_matrix)):
            if edge_matrix[current_index][neighbour] > 0:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)

    return False


graph = GraphAdjacencyMatrix(7)
graph.add_vertex(0, 'A')
graph.add_vertex(1, 'B')
graph.add_vertex(2, 'C')
graph.add_vertex(3, 'D')
graph.add_vertex(4, 'E')
graph.add_vertex(5, 'F')
graph.add_vertex(6, 'G')
 
graph.add_edge(0, 1)
# graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(3, 5)
graph.add_edge(2, 6)

print(has_path(graph, 0, 5))
print(has_path(graph, 1, 4))
print(has_path(graph, 2, 5))

