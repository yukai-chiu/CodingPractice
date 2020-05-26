# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#My first try
class Solution:
    def is_valid(self, node, max_val, min_val):
        if not node.left and not node.right:
            return (True, max(max_val, node.val), min(min_val, node.val))
        
        max_l = max_r = max_val
        min_l = min_r = min_val
        l = r = True
        if node.left:
            l, max_l, min_l = self.is_valid(node.left, max_val, min_val)
        if node.right:
            r, max_r, min_r = self.is_valid(node.right, max_val, min_val)
        if not l or not r:
            return (False, -1, -1)
        else:
            if max_l < node.val and node.val < min_r:
                return (True, max(max_r, node.val), min(min_l, node.val))
            else:
                return (False, -1, -1)
        
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        ans, _max, _min = self.is_valid(root, float('-inf'), float('inf'))
        print(ans, _max, _min)
        return ans
        



#Recursive
#Time: O(n)
#Space: O(n)
class Solution:
    def is_valid(self, node, max_val, min_val):
        if not node:
            return True
        if max_val <= node.val or node.val <= min_val:
            return False
        if not self.is_valid(node.left, node.val, min_val):
            return False
        if not self.is_valid(node.right, max_val, node.val):
            return False
        return True

               
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.is_valid(root, float('inf'), float('-inf'))
        

#Iterative
#Time: O(n)
#Space: O(n)
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = [(root, float('inf'), float('-inf'))]
        while stack:
            curr, upper, lower = stack.pop()
            if upper <= curr.val or curr.val <= lower:
                return False
            if curr.left:
                stack.append((curr.left, curr.val, lower))
            if curr.right:
                stack.append((curr.right, upper, curr.val))
        return True
        
        
#Inorder
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = []
        last = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop() 
            if root.val <= last:
                return False
            last = root.val
            root = root.right
            
        return True