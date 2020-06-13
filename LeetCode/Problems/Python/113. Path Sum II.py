# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Iterative DFS
#Time: O(n)
#Space:O (n)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return root
        
        stack = [(root, sum, [root.val])]
        result = []
        
        while stack:
            node, remain, path = stack.pop()
            remain -= node.val
            
            #if we found a leaf
            if not node.left and not node.right:
                if remain == 0:
                    result.append(path)
            if node.left:
                stack.append((node.left, remain, path + [node.left.val]))
            if node.right:
                stack.append((node.right, remain, path + [node.right.val]))
            
        return result
#dfs + backtracking 
#Time: O(n)
#Space:O (n)
class Solution:
    def dfs(self, node, remain, path):
        if not node:
            return
        #print(node.val, remain)
        remain -= node.val
        path.append(node.val)
        if not node.left and not node.right and remain == 0:
            #copy the found path
            self.result.append(path[:])
        if node.left:
            self.dfs(node.left, remain, path)
        if node.right:
            self.dfs(node.right, remain, path)
        #backtracking
        path.pop()
        return
        
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return root