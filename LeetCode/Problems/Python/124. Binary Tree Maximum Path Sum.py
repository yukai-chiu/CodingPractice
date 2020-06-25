#clean recursion
class Solution:
    def maxPath(self, node):
        if not node:
            return 0
        
        left = max(self.maxPath(node.left), 0)
        right = max(self.maxPath(node.right), 0)
        
        self.max_sum = max(self.max_sum, left+right+node.val)

        return max(left, right) + node.val
        
        
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
      
        self.max_sum = float('-inf')
        
        self.maxPath(root)
        
        return self.max_sum


#first try
class Solution:
    def maxPath(self, node):
        if not node:
            return None
        
        left = self.maxPath(node.left)
        right = self.maxPath(node.right)
        
        if left and right:
            
            self.max_sum = max(self.max_sum, left+right+node.val, node.val,max(left, right) + node.val)
            return max(left+ node.val, right+ node.val, node.val) 
        elif left:
            self.max_sum = max(self.max_sum, left+node.val, node.val)
            return max(left + node.val, node.val)
        elif right:
            self.max_sum = max(self.max_sum, right+node.val, node.val)
            return max(right + node.val, node.val)
        else:
            self.max_sum = max(self.max_sum, node.val)
            return node.val
        
        return max(left, right) + node.val
        
        
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
      
        self.max_sum = float('-inf')
        
        self.maxPath(root)
        
        return self.max_sum