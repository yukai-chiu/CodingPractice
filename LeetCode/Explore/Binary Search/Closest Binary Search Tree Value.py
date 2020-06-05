# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Time: O(h), h is the height of the tree
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return 0
        
        
        closet = float('inf')
        idx = 0
        while root:
            if abs(target - root.val) < closet:
                closet = abs(target - root.val)
                idx = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right

        return idx