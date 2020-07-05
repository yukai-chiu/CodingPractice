#Partial sorting with hashtable
#Time: O(nlog(n/k)), we have k cols, so we will do k sorting on each of (n/k)log(n/k) --> nlog(n/k), slightly faster than global sorting
#Space: O(n)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        queue = [(root, (0,0))]
        column_table = defaultdict(list)
        min_col = float('inf')
        max_col = float('-inf')
        while queue:
            for _ in range(len(queue)):
                cur, (col, row) = queue.pop(0)
                column_table[col].append((row,cur.val))
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                if cur.left:
                    queue.append((cur.left, (col-1, row+1)))
                if cur.right:
                    queue.append((cur.right, (col+1, row+1)))
        
        return [[val for row, val in sorted(column_table[col])] for col in range(min_col, max_col+1)]

#BFS + Global sorting
#Time: O(nlogn)
#Space: O(n)
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        queue = [(root, 0, 0)]
        nodes = []
        while queue:
            for _ in range(len(queue)):
                cur, col, row = queue.pop(0)
                nodes.append((col, row, cur.val))
                if cur.left:
                    queue.append((cur.left, col-1, row+1))
                if cur.right:
                    queue.append((cur.right, col+1, row+1))
                    
        nodes.sort()
        ans = defaultdict(list)
        for node in nodes:
            ans[node[0]].append(node[2])
            
        return ans.values()