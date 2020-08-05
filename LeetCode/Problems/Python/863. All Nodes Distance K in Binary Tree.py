#Time: O(n)
#Space: O(n)
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        #convert to graph and traverse
        if not root:
            return []
        
        graph = defaultdict(set)
        
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr.left:
                graph[curr.val].add(curr.left.val)
                graph[curr.left.val].add(curr.val)
                stack.append(curr.left)
            if curr.right:
                graph[curr.val].add(curr.right.val)
                graph[curr.right.val].add(curr.val)
                stack.append(curr.right)
        
        #bfs from target
        queue =deque()
        queue.append(target.val)
        visited = set()
        visited.add(target.val)
        ans = []
        while queue and K > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor) 
            K-=1

        return list(queue)
                
        
        