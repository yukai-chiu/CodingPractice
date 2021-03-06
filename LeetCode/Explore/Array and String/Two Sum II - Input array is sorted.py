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

#Second practive
#Two pointers
#Time: O(n)
#Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        
        l = 0
        r = len(numbers)-1
        while l < r:

            curr_sum = numbers[l] + numbers[r]
            #to prevent overflow
            #we should use:
            # if target-numbers[l] == numbers[r]
            if curr_sum == target:
                return [l+1,r+1]
            elif curr_sum > target:
                r-=1
            else:
                l+=1