class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = Counter()
        self.time_record = deque()
        self.count = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.data[timestamp]+=1
        self.count+=1
        if not self.time_record or timestamp != self.time_record[-1]:
            self.time_record.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.time_record and timestamp - 300 >= self.time_record[0]:
            expired = self.time_record.popleft()
            self.count-= self.data[expired]
            del self.data[expired]
        return self.count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)