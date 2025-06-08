# Eventual Safe States
# Asked in Companies:

# De Shaw

# Apple

# Sharechat

# Shipsy



# Description:
# You are given a directed graph of n nodes labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

# A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

# Your task is to return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.



# Input Parameters:

# graph (List[List[int]]): Adjacency list representing the directed graph.

# Output:

# List[int]: A list of safe nodes sorted in ascending order.



# Example:

# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
 
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]

# Steps
# 1. Identify all terminal nodes. Terminal Nodes are, by default, safe nodes.
# 2. For each node except the terminal nodes, find all possible paths starting from the node.
# 3. If any path ends in a node other than terminal node, mark False for that node, else True.
# 4. Return all nodes marked True.

def eventualSafeNodes(graph):
    """
    Function to find all the safe nodes in a directed graph.
    
    :param graph: List[List[int]] -> Adjacency list representing the directed graph
    :return: List[int] -> List of all safe nodes sorted in ascending order
    """
    # TODO: Implement the logic to find all safe nodes

    # 1. Identify all terminal nodes. Terminal Nodes are, by default, safe nodes.
    terminal_nodes = []
    nodes_state = [None for i in range(len(graph))]
    for node, nbr_lst in enumerate(graph):
        if len(nbr_lst)==0:
            terminal_nodes.append(node)
            nodes_state[node] = True
    # print(terminal_nodes)
    # 2. For each node except the terminal nodes, find all possible paths starting from the node.
    # 3. If any path ends in a node other than terminal node, mark False for that node, else True.
    for node in range(len(graph)):
        if node not in terminal_nodes:
            status = dfs(node, graph, terminal_nodes, [])
            nodes_state[node] = status

    # 4. Return all nodes marked True.
    safe_nodes = [index for index, state in enumerate(nodes_state) if state==True]

    return safe_nodes
    
def dfs(node, graph, terminal_nodes, path):
    
    
    print(node)
    if len(path) > 0:
        starting_node = path[0]
        if node == starting_node:
            return False
        
        if node in terminal_nodes: 
            return True
    
    path.append(node)
    
    
    for neighbour in graph[node]:
        if neighbour == node:
            return False
        input_path = path.copy()
        print(input_path)
        status = dfs(neighbour, graph, terminal_nodes, input_path)
        if not status:
            return status
    
    return status


# graph = [[1,2],[2,3],[5],[0],[5],[],[]]
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(eventualSafeNodes(graph))
    





