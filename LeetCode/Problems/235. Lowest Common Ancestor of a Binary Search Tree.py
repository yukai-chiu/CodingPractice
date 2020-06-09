#recursive
#Time: O(h), h is the height of tree, worst case the tree is unbalanced so it will be O(n)
#Space: O(h), same as above, call stack for recursion
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        #if we found one
        if root == p or root == q:
            return root
        
        #if the root is in the middle,
        #p and q are in left right subtree
        #then it is the LCA
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p,q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p,q)

#Iterative
#Time: O(h), h is the height of tree, worst case the tree is unbalanced so it will be O(n)
#Space: O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        
        curr = root
        
        while curr:
               
            #if we found one
            if curr == p or curr == q:
                return curr
            #if the root is in the middle,
            #p and q are in left right subtree
            #then it is the LCA
            elif p.val < curr.val < q.val or q.val < curr.val < p.val:
                return curr

            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right