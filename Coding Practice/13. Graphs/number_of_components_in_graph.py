from graph_using_adjacency_matrix import GraphAdjacencyMatrix
from collections import deque

def number_of_components_in_graph(graph):
    num_vertices = graph.num_vertices
    vertices = graph.vertices
    edge_matrix = graph.adj_matrix
    visited = []
    components = 0
    for index in range(num_vertices):
        if index not in visited:
            # traverse_dfs(index, visited, edge_matrix)
            traverse_bfs(index, visited, edge_matrix)
            components+=1
    
    return components

def traverse_dfs(index, visited, edge_matrix):
    current_index = index
    visited.append(index)
    for neighbour in range(len(edge_matrix)):
        if edge_matrix[current_index][neighbour] > 0:
            if neighbour not in visited:
                traverse_dfs(neighbour, visited, edge_matrix)

def traverse_bfs(start_index, visited, edge_matrix):
    queue = deque()
    queue.append(start_index)
    visited.append(start_index)

    while len(queue) != 0:
        current_index = queue.popleft()

        for neighbour in range(len(edge_matrix)):
            if edge_matrix[current_index][neighbour] > 0:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)

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
# graph.add_edge(3, 4)
graph.add_edge(4, 5)
# graph.add_edge(3, 5)
graph.add_edge(2, 6)

print(number_of_components_in_graph(graph))




