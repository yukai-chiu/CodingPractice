class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        hash_set = set()
        
        for n in nums:
            if n not in hash_set:
                hash_set.add(n)
            else:
                hash_set.remove(n)
        return list(hash_set)[0]