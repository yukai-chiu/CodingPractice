class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.myqueue = deque()
        if v1:
            self.myqueue.append(v1)
        if v2:
            self.myqueue.append(v2)
        

    def next(self) -> int:
        curr = self.myqueue.popleft()
        next_val = curr.pop(0)
        if curr:
            self.myqueue.append(curr)
        return next_val
    def hasNext(self) -> bool:
        return len(self.myqueue) 

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())