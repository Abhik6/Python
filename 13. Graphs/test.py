from graph_implementation_using_edge_list import *
from graph_implementation_using_adjacancy_list import *

# graph = GraphUsingEdgeList()

# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)
# graph.add_vertex(4)

# graph.add_edge(1,2)
# graph.add_edge(1,3)
# graph.add_edge(2,4)

# graph.display()

graph = GraphUsingAdjacencyList()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

graph.add_edge('A','B')
graph.add_edge('A','D')
graph.add_edge('B','D')
graph.add_edge('B','C')

graph.display()