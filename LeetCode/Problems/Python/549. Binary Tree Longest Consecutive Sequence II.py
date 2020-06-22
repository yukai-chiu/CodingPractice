# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return (0,0)
        incr = 1
        decr = 1
        
        if node.left:
            l = self.dfs(node.left)
            if node.val== node.left.val - 1:
                incr += l[0]
            elif node.val == node.left.val + 1:
                decr += l[1]
            
        if node.right:
            r = self.dfs(node.right)
            if node.val== node.right.val - 1:
                incr = max(incr, r[0]+1)
            elif node.val == node.right.val + 1:
                decr = max(decr, r[1]+1)
        self.max_seq = max(self.max_seq, incr+decr-1)
        return (incr, decr)
   
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        
        self.max_seq = 0
        self.dfs(root)
        
        return self.max_seq