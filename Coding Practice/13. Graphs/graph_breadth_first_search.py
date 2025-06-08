from collections import deque

class GraphAdjacencyMatrixDFS:
    def __init__(self, num_vertices):
        self.vertices = [None]*num_vertices
        self.adj_matrix = [[0]*num_vertices for i in range(num_vertices)]
        self.num_vertices = num_vertices

    def add_vertex(self, index, label):
        if index>=0 and index < self.num_vertices:
            self.vertices[index] = label
        else:
            print("Index OOB")
    
    def add_edge(self, source, destination, weight=1):
        if source>=0 and source < self.num_vertices and destination>=0 and destination < self.num_vertices:
            self.adj_matrix[source][destination] = weight
            self.adj_matrix[destination][source] = weight
        else:
            print("Index OOB")

    def display(self):
        
        result = self.display_BFS(0, [], [])
        return result

    def display_BFS(self, start_index=0, visited=[], result=[]):

        queue = deque()
        queue.append(start_index)
        visited.append(start_index)
        
        while len(queue) != 0:
            current_index = queue.popleft()
            result.append(self.vertices[current_index])
            for neighbour in range(self.num_vertices):
                if self.adj_matrix[current_index][neighbour] > 0:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.append(neighbour)
        
        return result


graph = GraphAdjacencyMatrixDFS(6)
graph.add_vertex(0, 'A')
graph.add_vertex(1, 'B')
graph.add_vertex(2, 'C')
graph.add_vertex(3, 'D')
graph.add_vertex(4, 'E')
graph.add_vertex(5, 'F')
 
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(3, 5)
 
print(graph.display())
