# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        
        
        queue = [root]
        lookUp = set()
        
        while queue:
            node = queue.pop()
            if not node:
                continue
            if k-node.val in lookUp:
                return True
            lookUp.add(node.val)
            queue.append(node.left)
            queue.append(node.right)
        return False