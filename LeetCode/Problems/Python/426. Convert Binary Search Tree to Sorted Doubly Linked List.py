class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        #inorder traversal
        
        if not root:
            return None
        
        head = None
        prev = None
        
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            
            if not head:
                head = curr
                prev = curr
            else:
                prev.right = curr
                curr.left = prev
                prev = curr
            curr = curr.right
        
        head.left = prev
        prev.right = head
        
        return head