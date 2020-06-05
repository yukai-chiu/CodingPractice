# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Time: O(n)
#Space: O(h), height of the tree
#"The successor of a node is the left-most node in its right sub-tree (if it exists). 
#Otherwise it is the first ancestor of the node whose left sub-tree contains the node."
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        #traverse inorder, if found p, mark it and return the next node
        if not root:
            return root
        
        stack = []
        successor = False
        while stack or root:
            while root: 
                stack.append(root)
                root = root.left
            root = stack.pop()
        
            if root == p:
                successor = True
            elif successor:
                return root
            root = root.right

