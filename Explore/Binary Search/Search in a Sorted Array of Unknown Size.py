# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l = 0
        r = 19999
        while l <= r:
            mid = l + (r-l)//2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) == 2147483647 or reader.get(mid) > target:
                r = mid -1
            else:
                l = mid + 1
                
        return -1
        