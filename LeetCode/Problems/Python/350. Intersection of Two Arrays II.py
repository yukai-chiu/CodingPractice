#hash map
#Time: O(m+n)
#Space: O(min(m,n))
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 or not nums2:
            return []
        
        intersect = []
        #make hash map for the smaller one
        #because the larger one will be bad for memory usage
        #in this problem, states num2 is large, on disk and cannot load all elements at once
        #so we should make hash table for nums1
        #
        #but we still compare the size here
        
        if len(nums1) <= len(nums2):
            nums1 = Counter(nums1)
            for n in nums2:
                if n in nums1 and nums1[n]>0:    
                    intersect.append(n)
                    nums1[n]-=1
        else:
            nums2 = Counter(nums2)
            for n in nums1:
                if n in nums2 and nums2[n]>0:    
                    intersect.append(n)
                    nums2[n]-=1

        return intersect


#If the input is sorted
#Time: O(nlogn + mlogm), this is for the sort, and we perform linear scan on it
#Space O (1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if not nums1 or not nums2:
            return []
        
        intersect = []
        #if the input is sorted
        nums1.sort()
        nums2.sort()
        
        p1 = 0
        p2 = 0
        
        while p1 <len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                intersect.append(nums1[p1])
                p1+=1
                p2+=1
            elif nums1[p1] < nums2[p2]:
                p1+=1
            elif nums1[p1] > nums2[p2]:
                p2+=1
            
        return intersect