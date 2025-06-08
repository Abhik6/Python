# Keys and Rooms
# Asked in Companies:

# Paypal
# Phonepe
# Wells Fargo
# Morgan Stanley


# Description
# You are given n rooms labeled from 0 to n - 1. All rooms are locked except for room 0, and each room contains a set of distinct keys. Each key has a number on it, denoting which room it unlocks, and you can collect and use all the keys in each room you visit.
# Your goal is to determine whether you can visit all the rooms, starting from room 0.


# Input:
# rooms: A list of lists where rooms[i] is a list of keys you can collect in room i.

# Output:
# Return True if you can visit all the rooms, otherwise return False.


# Example:

# Input:
# rooms = [[1], [2], [3], []]
 
# Output:
# True
 
# Explanation:
# - You start in room 0 and collect key 1.
# - You move to room 1 and collect key 2.
# - You move to room 2 and collect key 3.
# - You move to room 3, and all rooms are visited.
 
 
# Input:
# rooms = [[1, 3], [3, 0, 1], [2], [0]]
 
# Output:
# False
 
# Explanation:
# - You start in room 0 and collect keys 1 and 3.
# - Room 2 is never visited because you do not have its key.

def can_visit_all_rooms(rooms):
    
    n = len(rooms)
    visited = []

    visited = dfs(0, rooms, visited)

    if len(visited) == n:
        return True
    return False

def dfs(start_node, graph, visited=[]):

    visited.append(start_node)

    for neighbour in graph[start_node]:
        if neighbour not in visited:
            visited = dfs(neighbour, graph, visited)

    return visited

# Another Implementation
class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.
        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list
        return all(seen) # Return true iff we've visited every room

# rooms = [[1, 3], [3, 0, 1], [2], [0]]
rooms = [[1], [2], [3], []]
print(can_visit_all_rooms(rooms))
    