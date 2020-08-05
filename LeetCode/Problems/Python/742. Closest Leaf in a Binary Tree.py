#Time: O(n)
#Space: O(n)
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        graph =defaultdict(list)
        stack = [root]
        target = None
        while stack:
            curr = stack.pop()
            if curr.left:
                graph[curr.val].append(curr.left.val)
                graph[curr.left.val].append(curr.val)
                stack.append(curr.left)
            if curr.right:
                graph[curr.val].append(curr.right.val)
                graph[curr.right.val].append(curr.val)
                stack.append(curr.right)
                
                
        graph[root.val].append(None)
        queue = deque([k])
        closest_leaf = None
        dist = float('inf')
        
        visited = set()
        visited.add(k)
        
        while queue:
            curr = queue.popleft()
            
            if len(graph[curr]) == 1:
                return curr
            for neighbor in graph[curr]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

            
       
        
      