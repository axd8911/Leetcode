# BFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        curr = collections.deque([node])
        start = Node(node.val,[])
        curr_n = collections.deque([start])
        visited = set()
        exist = {node.val:start}

        while curr:
            for i in range(len(curr)):
                origin = curr.popleft()
                create = curr_n.popleft()
                if origin not in visited:
                    for neighbor in origin.neighbors:
                        if neighbor.val not in exist:
                            newNode = Node(neighbor.val,[])
                            exist[neighbor.val] = newNode
                            create.neighbors.append(newNode)
                            curr.append(neighbor)
                            curr_n.append(newNode)
                        else:
                            create.neighbors.append(exist[neighbor.val])
                    visited.add(origin)
        return start

# DFS iteration
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        curr = [node]
        start = Node(node.val,[])
        curr_n = [start]
        visited = set()
        exist = {node.val:start}

        while curr:
            for i in range(len(curr)):
                origin = curr.pop()
                create = curr_n.pop()
                if origin not in visited:
                    for neighbor in origin.neighbors:
                        if neighbor.val not in exist:
                            newNode = Node(neighbor.val,[])
                            exist[neighbor.val] = newNode
                            create.neighbors.append(newNode)
                            curr.append(neighbor)
                            curr_n.append(newNode)
                        else:
                            create.neighbors.append(exist[neighbor.val])
                    visited.add(origin)
        return start

# DFS Recursion
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        start = Node(node.val,[])
        visited = set()
        exist = {node.val:start}
        def dfs(node,output):
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor.val not in exist:
                    new = Node(neighbor.val,[])
                    exist[neighbor.val] = new
                    output.neighbors.append(new)
                else:
                    output.neighbors.append(exist[neighbor.val])
                if neighbor not in visited:
                    dfs(neighbor,new)
            return output
        return dfs(node, start)
