class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers: 
            return []
        l = 0
        r = len(numbers) -1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
        