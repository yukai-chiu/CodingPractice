# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#recursive solution 
class Solution:
    def helper(self, node, in_order):
        #traverse to the left most leaf
        if node.left:
            self.helper(node.left, in_order)
        #if found, append to the result    
        in_order.append(node.val)
        #traverse the right subtree
        if node.right:
            self.helper(node.right, in_order)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        in_order = []
        self.helper(root, in_order)
        
        return in_order

#iterative solution
class Solution:  
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        stack = []
        in_order = []
      
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            in_order.append(curr.val)

            curr = curr.right

        return in_order
                
