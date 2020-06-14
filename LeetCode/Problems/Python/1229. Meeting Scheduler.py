#Time: O(nlogn)
#Space: O(n)
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        #pick from each person, and start = 1, end = -1,
        #when it's changing from 2 to 1, we calculate if the time interval > duration
        
        
        #sort by start time
        
        slots1.sort(key = lambda x :x[0])
        slots2.sort(key = lambda x :x[0])
        
        p1 = 0
        p2 = 0
        
        while p1 < len(slots1) and p2 < len(slots2):
            start = max(slots1[p1][0], slots2[p2][0])
            end = min(slots1[p1][1], slots2[p2][1])
            
            if start + duration <= end:
                return [start, start+duration]
            
            #move the pointer
            #we compare which ends first
            #because the next available time for that person could form a result or overlap
            if slots1[p1][1] < slots2[p2][1]:
                p1+=1
            else:
                p2+=1
        return []

#first try
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        #pick from each person, and start = 1, end = -1,
        #when it's changing from 2 to 1, we calculate if the time interval > duration
        
        
        #preprocess the data
        p1 = []
        p2 = []
        for s in slots1:
            p1.append((s[0],1))
            p1.append((s[1],-1))
        
        for s in slots2:
            p2.append((s[0],1))
            p2.append((s[1],-1))
        p1.sort()
        p2.sort()    
        available = 0    
        start = 0

        while p1 and p2:
            if p1[0][0] < p2[0][0]:
                t = p1.pop(0)
            else:
                t = p2.pop(0)
            #print(t)
            if t[1] == 1:
                start = t[0]
            if available == 2 and t[0] - start >=duration:
                return [start, start+duration]
    
            available += t[1]
        
        return []