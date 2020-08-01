#Time: O(H+k)
#Space: O(H)
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0
        
        #preorder to k
        stack = []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k-=1
            if k==0:
                return curr.val
            curr = curr.right
                
        
        return -1