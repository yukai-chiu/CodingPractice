class Solution:
    def dfs(self, node, root):
        if not node:
            return True
        if not root:
            return False

        return node.val == root.val and (self.dfs(node.next, root.left) or self.dfs(node.next, root.right))
      
        
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not head:
            return True
        if not root:
            return False
        
        #find the starting point
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

class Solution:
    def dfs(self, node, root):
        if not node:
            return True
        
        if root and node.val == root.val:
            return self.dfs(node.next, root.left) or self.dfs(node.next, root.right)
      
        return False
        
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        if not root or not head:
            return False
        
        stack = [root]
        
        #find the starting point
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            if curr.val == head.val:
                if self.dfs(head, curr):
                    return True
            stack.append(curr.left)
            stack.append(curr.right)
        
        return False

