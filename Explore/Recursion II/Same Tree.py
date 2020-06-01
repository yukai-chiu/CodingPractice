# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def checkSame(p,q):
            if not q and not p:
                return True
            if not q or not p:
                return False
            if q.val != p.val:
                return False
            return True
        
        if not q and not p:
            return True
        if not q or not p:
            return False
        
        if q.val != p.val:
            return False
        
        deq = collections.deque()
        
        deq.append((p,q))
        
        while deq:
            p, q = deq.popleft()
            if checkSame(p,q):
                if p:
                    deq.append((p.right,q.right))
                    deq.append((p.left,q.left))
            else:
                return False
        return True
                
        