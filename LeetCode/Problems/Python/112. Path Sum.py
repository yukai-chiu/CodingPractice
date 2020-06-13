#Old implementation
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        queue = [(root,sum)]
        
        while queue:
            curr, sum = queue.pop()
            sum -= curr.val
            if not curr.left and not curr.right and sum == 0:
                return True
            
            if curr.left:
                queue.append((curr.left, sum))
            if curr.right: 
                queue.append((curr.right, sum))
            
        return False

#DFS
#Time: O(n)
#Space: O(n)
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return root
        
        #dfs
        stack = [(root, sum)] 
        
        while stack:
            node, remain = stack.pop()
            if not node:
                continue
            remain -= node.val
            if not node.left and not node.right:
                if remain == 0:
                    return True
            else:
                stack.append((node.right, remain))
                stack.append((node.left, remain))
        
        return False