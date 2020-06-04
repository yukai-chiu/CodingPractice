#Heap
#Time: O(m*n*log(mn))
#Space: O(m*n)
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0
        
        #similar concept as 1d trapped water
        #the 1d two pointers method use the smallest boundary to trap the water and walk step by step
        #to the middle
        #but in this 2d version, we have more boundaries, if we still want the same behavior
        #we can use a priority queue or min heap to achieve it
        #start from the smallest boundary and walk into the region
        #at each step, we can caculate the trapped water amount and add the node to the queue with
        #it's updated water height and row,col
        boundary = []
        #we also want to keep track of the visited node so we don't do duplicate calculation
        visited = set()
        
        trapped = 0
        #first we initial the heap with the boundary
        for i in range(len(heightMap)):
            for j in range(len(heightMap[0])):
                if i == 0 or i == len(heightMap)-1 or j == 0 or j == len(heightMap[0])-1:
                    heapq.heappush(boundary,(heightMap[i][j],i,j))
                    visited.add((i,j))
        #this is the 4 directions we are going to walk            
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        
        #go through the heap
        while boundary:
            #find the smallest height
            h, x, y = heapq.heappop(boundary)
            #check 4 neighbors
            for d in direction:
                x_d = x+d[0]
                y_d = y+d[1]
                #if it is in the map and not visited 
                if 0<=x_d<len(heightMap) and 0<=y_d<len(heightMap[0]) and (x_d,y_d) not in visited:
                    #we see if we can trap water at the point
                    #this is because of if it is smaller than our current boundary
                    #it will always be bounded by this height since we are using a min heap
                    #the current boundary will always be the smallest
                    trapped += max(0,h - heightMap[x_d][y_d])
                    #we push the neighbor into the heap with it's updated height
                    #this will spend O(logmn) at worst case
                    #since we have mn indices to check and it's the cost of pushing into a heap
                    heapq.heappush(boundary,(max(h,heightMap[x_d][y_d]),x_d,y_d))
                    #and add it to visited
                    visited.add((x_d,y_d))
                
        return trapped
        