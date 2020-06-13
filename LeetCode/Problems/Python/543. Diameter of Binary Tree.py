#DFS
#Time: O(n)
#SpaceL O(n)
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.ans = max(self.ans, right+left+1)
        return max(left,right)+1
        
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.ans = float(-inf)
        self.dfs(root)
        
        #ans is the count of node, and we want to return the count of edge
        return self.ans-1