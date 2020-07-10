class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        
        cloneMap = {}
        
        root = Node(node.val)
        cloneMap[node] = root
        visited = set()
        visited.add(node)
        queue = deque()
        #bfs
        queue.append((node, root))
        while queue:
            ref, curr = queue.pop()
            for neighbor in ref.neighbors:
                if neighbor in cloneMap:
                    clone_neighbor = cloneMap[neighbor]
                else:
                    clone_neighbor = Node(neighbor.val)
                    cloneMap[neighbor] = clone_neighbor
                curr.neighbors.append(clone_neighbor)
                
                if neighbor not in visited:
                    queue.append((neighbor, clone_neighbor))
                    visited.add(neighbor)
        
        return root

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
