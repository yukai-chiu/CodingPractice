"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':      
        
        if not node:
            return None 

        root = Node(1)
        visited = {root.val:root}
        self.dfs(node, visited)
        
        
        return visited[1]
        
        
        
    def dfs(self, node, visited):
        if not node.neighbors:
            return

        for n in node.neighbors:    
            if n.val not in visited:
                visited[n.val] = Node(n.val)
                visited[node.val].neighbors.append(visited[n.val])
                self.dfs(n, visited)
            else:
                visited[node.val].neighbors.append(visited[n.val])
