#Top down iterative DFS
#Time: O(n)
#Space: O(n)
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_seq = 0
        
        stack = []
        stack.append((root, 1))
        
        while stack:
            curr, length = stack.pop()
            max_seq = max(max_seq, length)
            if curr.left:
                if curr.left.val == curr.val+1:
                    stack.append((curr.left, length+1))
                else:
                    stack.append((curr.left, 1))
            if curr.right:
                if curr.right.val == curr.val+1:
                    stack.append((curr.right, length+1))
                else:
                    stack.append((curr.right, 1))
        return max_seq


#bottom up recursion
#Time: O(n)
#SpaceL O(n)
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        
        #add 1 for the current node
        l = self.dfs(node.left) + 1
        r = self.dfs(node.right) + 1
        
        #and check if we have to reset it to 1
        if node.left and node.val+1 != node.left.val:
            l = 1
        if node.right and node.val+1 != node.right.val:
            r = 1
            
        length = max(l,r)
        self.max_seq = max(self.max_seq, length)
        return length
        
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_seq = 0
        self.dfs(root)
        return self.max_seq