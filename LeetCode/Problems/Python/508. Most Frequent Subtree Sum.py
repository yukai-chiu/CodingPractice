#Time: O(n)
#Space: O(n)
class Solution:
    def dfs(self, node, subtree_sum):
        if not node:
            return 0
        
        s = node.val + self.dfs(node.left, subtree_sum) + self.dfs(node.right, subtree_sum)
        subtree_sum[s]+=1
        
        return s
    
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        subtree_sum = Counter()
        self.dfs(root, subtree_sum)
        max_freq = max(subtree_sum.values())
              
        return [x for x in subtree_sum if subtree_sum[x] == max_freq]