#Boyer-Moore Voting Algorithm
#Time: O(n)
#Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = 0
        count2 = 0
        candidate1 = None
        candidate2 = None
        
        for num in nums:
            
            if num == candidate1:
                count1+=1
            elif num == candidate2:
                count2+=1                
            elif count1 == 0:
                candidate1 = num
                count1+=1
            elif count2 == 0:
                candidate2 = num
                count2+=1
            else:
                count1-=1
                count2-=1
                            
        
        ans = []

        if nums.count(candidate1) > len(nums)//3:
            ans.append(candidate1)
        if nums.count(candidate2) > len(nums)//3:
            ans.append(candidate2)
        return ans