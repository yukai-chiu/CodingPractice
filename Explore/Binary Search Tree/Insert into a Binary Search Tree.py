# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Recursive
#Time:O(h)
#Space: O(h)
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode(val)
            return root
        
        if not root.left and root.val > val:
            root.left = TreeNode(val)
            return root
            
        elif not root.right and root.val < val:
            root.right = TreeNode(val)
            return root
        
        if root.val > val:
            self.insertIntoBST(root.left,val)
        else:
            self.insertIntoBST(root.right,val)
        
        
        return root
            
#Iterative
#Time:O(h)
#Space: O(1)           
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            root = TreeNode(val)
            return root
 
        curr = root
        while curr:
            if curr.val > val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                else:
                    curr = curr.left

            elif curr.val < val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                else:
                    curr = curr.right

        return root