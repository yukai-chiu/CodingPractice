#hash + binary search
#Time: O(1) for set, O(logn) for get
#Space: O(n)
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #make sure there's a value
        arr = self.timeMap.get(key)
        if arr is None:
            return ""
        
       
        l = 0 
        r = len(arr)
        
        #we are finding the right bound of the timestamp
        while l < r:
            mid = l + (r-l)//2
            if arr[mid][0] <= timestamp:
                l = mid + 1
            elif arr[mid][0] > timestamp:
                r = mid
        if r == 0:
            return ""
        return arr[r-1][1]


#hash + linear search
#Time limit exceeded
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #make sure there's a value
        desired = self.timeMap.get(key)
        if desired is None:
            return ""
        
        if timestamp < desired[0][0]:
            return ""
        #linear search - brute force

        for i, t in enumerate(desired):
            if t[0] > timestamp:
                return desired[i-1][1]
        return desired[-1][1]