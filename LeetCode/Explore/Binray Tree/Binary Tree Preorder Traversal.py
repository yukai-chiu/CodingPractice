# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        def helper(root, result):
            
            if not root:
                return
            result.append(root.val)
            helper(root.left, result)
            helper(root.right, result)
   
        if not root:
            return []
        
        result = []
        helper(root, result)
        
        return result

#iterative
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            curr = stack.pop()
            if curr:
                result.append(curr.val)
                if curr.right:
                    stack.append(curr.right) 
                if curr.left:
                    stack.append(curr.left) 
        return result