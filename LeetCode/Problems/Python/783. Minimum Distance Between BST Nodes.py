#Time: O(n)
#Space: O(H)
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        #inorder traversal
        if not root:
            return 0
        
        node = root
        stack = []
        min_distance = float('inf')
        inorder = []
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if prev is None:
                prev = node.val
            else:
                min_distance = min(min_distance, node.val-prev)
                prev = node.val
            node = node.right
    
        return min_distance
#Time: O(n)
#Space: O(n)
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        #inorder traversal
        if not root:
            return 0
        
        curr = root
        stack = []
        min_distance = float('inf')
        inorder = []
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            inorder.append(curr.val)
            curr = curr.right
        
        for i in range(1,len(inorder)):
            min_distance = min(min_distance, inorder[i]-inorder[i-1])
        
        return min_distance