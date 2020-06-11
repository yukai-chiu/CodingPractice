#Time: O(nlogn)
#Space: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        #thought:
        #everytime we pick start, we need to add a new room
        #if we pick end, we can decrease the room count
        #keep track the max count
        

        meet_queue = []
        for i in intervals:
            meet_queue.append((i[0],1))
            meet_queue.append((i[1],-1))
        
        max_room = 0

        room = 0
        meet_queue.sort()
        for m in meet_queue:
            room += m[1]
            max_room = max(max_room,room)    
        
       
                
        return max_room
            
#Priority queue
#Time: O(nlogn)
#Space: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        room = []
        
        intervals.sort()
        
        for i in intervals:
            #use min heap to store the end time
            #if the end time is earlier or the same as the new meeting
            #we can pop it and add all the end time of ongoing meetings to the heap
            if room and room[0] <= i[0]:
                heapq.heappop(room)
            heapq.heappush(room,i[1])

        return len(room)