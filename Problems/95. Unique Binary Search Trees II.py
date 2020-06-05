# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def gen(self,va,memo):
        if va == []:
            return [None]
        if len(va)==1:
            return [TreeNode(va[0])]
        
        if tuple(va) in memo:
            return memo[tuple(va)]
        res = []
        #for loop, every i can be the root
        for i,v in enumerate(va):
            left = self.gen(va[:i],memo)
            right = self.gen(va[i+1:],memo)
            for l in left:
                for r in right:
                    curr = TreeNode(v)
                    curr.left = l
                    curr.right = r
                    res.append(curr)
        memo[tuple(va)] = res
        return memo[tuple(va)]
            
        
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        #divide and conquer
        
        
        #base case: if 0 --> return None
        #base case: if 1 --> return 1 node
        #left = recursion, left subtree
        #right = recursion right subtree
        
        #nested for loop to combine them together into a list and return
        #print(n)
        
        #v = [x for x in range(1,n+1)]
        v= []
        for x in range(1,n+1):
            v.append(x)
        ans = self.gen(v,{})
        return ans