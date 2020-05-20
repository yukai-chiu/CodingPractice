# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node, result):   
            if node.left:
                helper(node.left, result)
            if node.right:
                helper(node.right, result)
            result.append(node.val)
            
        if not root:
            return root
        
        result = []
        helper(root,result)
        
        return result

#iterative
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        
        stack = [root]
        result = []
        while stack:
            curr = stack.pop()
            result.insert(0, curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return result