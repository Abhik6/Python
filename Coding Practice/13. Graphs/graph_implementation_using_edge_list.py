class GraphUsingEdgeList:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            return f"Vertex '{vertex}' added to graph"
        else:
            return f"Vertex '{vertex}' already present in graph"
        
    def add_edge(self, source, destination, weight=1):
        if source in self.vertices and destination in self.vertices:
            self.edges.append((source, destination, weight))
        else:
            return f" One or both of the vertices not present in graph"
        
    def display(self):
        for vertex in self.vertices:
            print(f"Vertex: {vertex}")
        
        for source, destination, weight in self.edges:
            print(f"{source} --> {destination}")





