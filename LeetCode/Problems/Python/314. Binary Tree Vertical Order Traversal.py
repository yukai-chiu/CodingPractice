#Time:O(n)
#Space: O(n)
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        columnTable = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        min_col = float('inf')
        max_col = float('-inf')
        while queue:
            cur, col = queue.popleft()
            if not cur:
                continue
            columnTable[col].append(cur.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            queue.append((cur.left, col-1))
            queue.append((cur.right, col+1))
        
        return [columnTable[col] for col in range(min_col, max_col+1)]