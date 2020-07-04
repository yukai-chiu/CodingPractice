#First try iterative + stack
#Time: O(n)
#Space: O(n)
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        stack = []
        stack.append(root.right)
        
        stack.append(root.left)
        root.left = None
        flat_ptr = root
        
        while stack:
            curr = stack.pop()
            if not curr:
                continue

            if curr != flat_ptr.right:

                flat_ptr.right = curr
                flat_ptr = flat_ptr.right
            else:
                flat_ptr = curr

            
            stack.append(curr.right)
            
            stack.append(curr.left)
            curr.left = None
            