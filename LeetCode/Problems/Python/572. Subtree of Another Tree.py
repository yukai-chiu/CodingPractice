#Time: O(m*n) worst case
#Space: O(n), if n is skewed tree
class Solution:
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not t or not s:
            return False
        
        return s.val == t.val and self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        
        
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not t or not s:
            return False
            
        equal = False

        if s.val == t.val:
            equal = self.sameTree(s, t)

        #search
        return equal or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        