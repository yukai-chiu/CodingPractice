class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        for n in nums:
            digit = 0
            while n > 0:
                n = n // 10
                digit +=1
            if digit % 2 == 0:
                count += 1
                
        return count