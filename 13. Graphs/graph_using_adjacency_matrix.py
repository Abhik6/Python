class GraphUsingAdjacencyMatrix:
    def __init__(self, num_vertices):
        self.V = {}
        self.edge_matrix = [[0]*num_vertices for i in range(num_vertices)]
        self.num_vertices = num_vertices

    def add_vertex(self, index, label):
        if index>=0 and index <= self.num_vertices:
            if label not in self.V.values() and index not in self.V:
                self.V[index] = label
            elif label not in self.V.values() and index in self.V:
                print(f"Index {index} already in use")
            else:
                print(f"Vertex {label} already present")
        else:
            print("Index OOB")
    
    def add_edge(self, source, destination, weight=1):
        if source in self.V and destination in self.V:
            self.edge_matrix[source][destination] = weight
            self.edge_matrix[destination][source] = weight
        else:
            print("Index OOB")

    def display(self):
        for index, label in self.V.items():
            print(f"Vertex Index: {index}, label: {label}")
        for row in self.edge_matrix:
            print(row)


## Another Implementation

class GraphAdjacencyMatrix:
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
        for index, label in enumerate(self.vertices):
            print(f"Vertex Index: {index}, label: {label}")
        for row in self.adj_matrix:
            print(row)

