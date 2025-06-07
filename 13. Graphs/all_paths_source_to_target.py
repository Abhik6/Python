# All paths from source to target
# Asked in Companies:

# American Express
# Cisco
# Make my Trip
# Salesforce


# Description:
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, you need to find all possible paths from node 0 to node n - 1. The graph is represented as an adjacency list where graph[i] contains a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to each node in graph[i]). The graph is guaranteed to be a DAG. Return all possible paths from node 0 to node n - 1 in any order.


# Input Parameters:
# graph (List[List[int]]): An adjacency list where graph[i] represents the nodes that can be reached from node i.

# Output:
# Return a list of all possible paths from node 0 to node n - 1.


# Example:

# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two possible paths from node 0 to node 3.
 
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,4],[0,1,3,4],[0,1,2,3,4]]
# Explanation: All possible paths from node 0 to node 4.

def all_paths_source_target(graph):
    """
    Function to find all possible paths from node 0 to node n - 1 in a DAG.
    
    :param graph: List[List[int]] -> Adjacency list representing the DAG
    :return: List[List[int]] -> List of all possible paths from node 0 to node n - 1
    """
    # TODO: Implement the logic to find all paths from source to target
    
    start_node = 0
    end_node = len(graph)-1

    paths = dfs(start_node, end_node, graph, [])

    return paths



def dfs(start_node, end_node, graph, path=[]):
    
    result_paths = []
    path.append(start_node)

    if start_node == end_node:
        result_paths.append(path)
        return result_paths
    
    for neighbour in graph[start_node]:
        # print(start_node)
        # print(neighbour)
        # print()
        input_path = path.copy()
        paths = dfs(neighbour, end_node, graph, input_path)
        for child_path in paths:
            result_paths.append(child_path)

    return result_paths

# graph = [[1,2],[3],[3],[]]
graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(all_paths_source_target(graph))



