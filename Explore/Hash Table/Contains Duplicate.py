class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        hash_set = set()
        for n in nums:
            if n not in hash_set:
                hash_set.add(n)
            else:
                return True
        return False