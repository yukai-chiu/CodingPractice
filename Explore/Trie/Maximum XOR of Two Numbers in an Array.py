class Trie(object):
    def __init__(self):
        self.child = {}
        self.value = None
        

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        ans = float('-inf')
        root = Trie()
        
        #initial the trie
        for n in nums:
            curr = root
            for i in range(30,-1,-1):
                curbit = (n >> i) & 1
                curr = curr.child.setdefault(curbit,Trie())
            curr.value = n
        #find the ans
        for n in nums:
            curr = root
            for i in range(30,-1,-1):
                curbit = (n >> i) & 1
                if (curbit ^ 1) in curr.child:
                    curr = curr.child[curbit ^ 1]
                else:
                    curr = curr.child[curbit]
                
            ans = max(ans, n ^ curr.value)
        
        return ans
        
                
        