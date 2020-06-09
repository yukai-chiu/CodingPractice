# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #intuition:
        #dfs or bfs to find both nodes
        #store the path 
        #start from comparing 
        #pop the one with longer path
        #until they have same length of path --> same level
        #if value not the same, pop one for each --> take a step to parent
        #if equal --> return
        
        #maybe use a stack to do backtracking with dfs
        
        
        #let's first do it in a recursive way
        #traverse the tree
        #if we reach child of the leaf
        #return None
        if not root:
            return None
        
        #if we found it
        if root==p or root==q:
            return root
        
        #recursive
        l = self.lowestCommonAncestor(root.left,p,q)
        r = self.lowestCommonAncestor(root.right,p,q)
        
        #if the current one is the lowest common ancester
        #then we may have value in left and right
        if l and r:
            return root
        #if only one have value,
        #let's say l, then no p or q exist in r subtree
        #so we return l
        #note that the case than p is under q will be handled
        #because we found p first and not found q, then q must be under p
        #so we return p
        elif l:
            return l
        else:
            return r
        
        
       
        
        
                
        