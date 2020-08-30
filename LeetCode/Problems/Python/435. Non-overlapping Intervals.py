class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        remove_count = 0
        
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        for i in intervals:
            if i[0] >= end:
                end = i[1]
            else:
                remove_count+=1
        
        return remove_count