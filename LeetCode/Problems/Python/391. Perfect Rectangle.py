class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        #1. sum of area of all small should equal to large
        #2. all node should appear twice except corner for max rect, it shuold be once
        if not rectangles:
            return False
        
        nodes = Counter()
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        max_area = 0
        sum_area = 0
        for rect in rectangles:
            #4 nodes
            nodes[(rect[0], rect[1])]+=1
            nodes[(rect[0], rect[3])]+=1
            nodes[(rect[2], rect[1])]+=1
            nodes[(rect[2], rect[3])]+=1
            sum_area += (rect[2]-rect[0]) * (rect[3]-rect[1])
            
            #get max corner
            min_x = min(min_x, rect[0])
            min_y = min(min_y, rect[1])
            max_x = max(max_x, rect[2])
            max_y = max(max_y, rect[3])
            
        
        max_area = (max_x - min_x) * (max_y - min_y)
        print(sum_area, max_area)
        if sum_area != max_area:
            return False
        print(nodes, min_x, min_y, max_x, max_y)
        if not nodes.pop((max_x, max_y), False):
            return False 
        if not nodes.pop((min_x, max_y), False):
            return False 
        if not nodes.pop((min_x, min_y), False):
            return False 
        if not nodes.pop((max_x, min_y), False):
            return False 
        print(nodes, min_x, min_y, max_x, max_y)
        for n in nodes:
            if nodes[n] %2!=0:
                return False
        return True