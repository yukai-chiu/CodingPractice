# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#iterative
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
    
        queue = [root]
        ans = 0
        
        while queue:
            ans += 1
            for i in range(len(queue)):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
        return ans
        
#recursive
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        def max_depth(node, depth):
            if not node:
                return depth
            depth +=1
            l = max_depth(node.left, depth)
            r = max_depth(node.right, depth)
            
            return max(l,r)
        
        if not root:
            return 0
        return max_depth(root, 0)
        
        