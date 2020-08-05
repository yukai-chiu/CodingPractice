class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        min_distance = float('inf')
        prev = None
        curr = root
        stack = []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev == None:
                prev = curr.val
            else:
                min_distance = min(min_distance, curr.val-prev)
                prev = curr.val
            curr = curr.right
        return min_distance