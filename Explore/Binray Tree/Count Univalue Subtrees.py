# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalue(self, node):
        
        if not node.left and not node.right:
            self.count += 1
            return True
        
        is_uni = True
        
        if node.left:
            is_uni = self.isUnivalue(node.left) and is_uni and node.left.val == node.val
            
        if node.right:
            is_uni = self.isUnivalue(node.right) and is_uni and node.right.val == node.val
        
        self.count += is_uni
        return is_uni
    


    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        self.count = 0 
        self.isUnivalue(root)
        return self.count
        