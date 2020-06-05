# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursive
class Solution:
    def is_mirror(self, t1, t2):
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        return t1.val == t2.val and self.is_mirror(t1.left, t2.right) and self.is_mirror(t1.right, t2.left)
        
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        return self.is_mirror(root, root)

#iterative

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        queue = [root,root]
        
        while queue:
            l = queue.pop(0)
            r = queue.pop(0)

            if l.val != r.val:
                return False
            else:
                if l.right and r.left:
                    queue.append(l.right)
                    queue.append(r.left)
                elif l.right or r.left:
                    return False

                if l.left and r.right:
                    queue.append(l.left)
                    queue.append(r.right)
                elif l.left or r.right:
                    return False
        return True