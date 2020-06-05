# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive
class Solution:
    def getSum(self, root, sum):
        if not root:
            return False
   
        sum -= root.val
        
        if not root.left and not root.right:
            return sum == 0

        return self.getSum(root.left, sum) or self.getSum(root.right, sum)
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        
        
        if not root:
            return False
        
        return self.getSum(root, sum)


#iterative
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        queue = [(root,sum)]
        
        while queue:
            curr, sum = queue.pop()
            sum -= curr.val
            if not curr.left and not curr.right and sum == 0:
                return True
            
            if curr.left:
                queue.append((curr.left, sum))
            if curr.right: 
                queue.append((curr.right, sum))
            
        return False