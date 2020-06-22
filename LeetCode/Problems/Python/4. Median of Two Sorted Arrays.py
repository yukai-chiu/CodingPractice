#Binary Search
#Time: O(log(min(m,n)))
#Space: O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        #we want to search in the smaller list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1;
            
        M = len(nums1)
        N = len(nums2)
        
        #if N == 0:
        #    raise ValueError

        #binary search in 1 and check if we can find it
        lo = 0
        hi = M
        
        while lo <= hi:
            i = lo + (hi-lo)//2
            j = (M+N+1)//2 - i
            print(i,j)
            if i < M and nums2[j-1] > nums1[i]:
                #i is too small, we want to move to the right
                lo = i+1
            elif i >0 and nums1[i-1] > nums2[j]:
                #i is too big, we want to move to the left
                hi = i-1
                
            else:#
                if i == 0:
                    max_left = nums2[j-1]
                elif j==0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums1[i-1], nums2[j-1])
                
                #if it is odd, left will have one more element and it will be the answer
                if(M+N) % 2 == 1:
                    return max_left
                    
                if i == M:
                    min_right = nums2[j]
                elif j == N:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])
                    
                
                return (min_right + max_left)/2
            
            
      
 