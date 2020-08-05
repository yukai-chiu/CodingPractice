# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        level_order = deque()  
        queue = deque([root])
        
        while queue:
            curr_level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if not curr:
                    continue
                curr_level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            if curr_level:
                level_order.appendleft(curr_level)
        return list(level_order)