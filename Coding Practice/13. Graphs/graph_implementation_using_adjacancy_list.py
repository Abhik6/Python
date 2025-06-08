class GraphUsingAdjacencyList:
    def __init__(self):
        self.vertices = []
        self.edges = {}
    

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            self.edges[vertex] = []
        else:
            print(f"Vertex {vertex} already present in graph")


    def add_edge(self, source, destination, weight=1):
        if source in self.vertices and destination in self.vertices:
            self.edges[source].append((destination, weight))
            self.edges[destination].append((source, weight))
        else:
            print(f"One or both vertices not present in graph")

    
    def display(self):
        print("Vertices")
        for vertex in self.vertices:
            print(f"Vertex: {vertex}")
        print("Edges")
        for vertex, edges in self.edges.items():
            print(f"{vertex} --> {edges}")


