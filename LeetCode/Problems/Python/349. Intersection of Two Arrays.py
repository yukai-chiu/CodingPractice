class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        intersect = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        if len(nums1) < len(nums2):
            for n in nums1:
                if n in nums2:
                    intersect.append(n)
        else:
            for n in nums2:
                if n in nums1:
                    intersect.append(n)

        return intersect