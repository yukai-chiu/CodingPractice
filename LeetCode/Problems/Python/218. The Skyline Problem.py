#Heap + sort
#Time: O(nlogn)
#Space: O(n)
class Solution(object):
    def getSkyline(self, buildings):
        
        #we want to sort by height so put H in front
        #we want to separate L and R, so set height of R as 0
        #since if it's the end, it will be (R,0)
        critical_pts = [[L, -H, R] for L, R, H in buildings]
        critical_pts.extend([[R, 0, 0] for L, R, H in buildings])
        critical_pts.sort()
        
        #we can use a heap to track the current alive building during the scan from left to right
        #so we initial the result and alive list with default value
        #result:[x, height]
        #initial with one item for more general algo
        result = [[0,0]]
        
        #heap 
        #[-height, ending position]
        alive = [(0, float('inf'))]        
        
        
        for pos, negH, R in critical_pts:
            #step 1: check if any building aready end?
            while alive[0][1] <= pos:
                heapq.heappop(alive)
            #step 2: if the current pt starts a new building
            if negH < 0:
                heapq.heappush(alive, (negH, R))
                #print(alive)

            #step 3: check if we need to add new pt to result
            #        we can see if the height change, because it indicates
            #        1. new building 
            #        2. we've passed old building's R
            if result[-1][1] != -alive[0][0]:
                result.append([pos, -alive[0][0]])
            
        return result[1:]