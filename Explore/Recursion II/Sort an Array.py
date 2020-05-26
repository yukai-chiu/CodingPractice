#Merge sort, recursive
#Time: O(nlogn), to merge two sorted list, it's O(n), and we did it O(logn) times
#Space: O(n), n elements to store the result
class Solution:
    def merge(self, left, right):
        l_p = r_p = 0
        result = []
        while l_p < len(left) or r_p < len(right):
            if left[l_p] <= right[r_p]:
                result.append(left[l_p])
                l_p+=1
            else:
                result.append(right[r_p])
                r_p+=1
        if l_p < len(left):
            result.extend(left[l_p:])
        elif r_p < len(right):
            result.extend(right[r_p:])
        
        return result
        
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        pivot = len(nums)//2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])
        #merge the sorted array in linear time 
        return merge(left, right)