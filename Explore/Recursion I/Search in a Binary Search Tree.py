# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive
#Time: O(h), h as height of the tree, average case: O(logn), worst case: O(n), n is the number of the nodes
#Space: O(h), h as height of the tree, average case: O(logn), worst case: O(n), n is the number of the nodes
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if not root:
            return None
        if root.val == val:
            return root
        
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)

#Iterative
#Time: O(h), h as height of the tree, average case: O(logn), worst case: O(n), n is the number of the nodes
#Space: O(1)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left   
        return None
