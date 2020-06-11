#Sorting
#Time: O(nlogn)
#Space: O(1)
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #intuition:
        #make sure there's no overlapping
        ##if we can sort the starting time
        #we can check the max ending time
        #if the current starting is earlier than the max ending time
        #than return false
        if not intervals:
            return True
        
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
            
        return True