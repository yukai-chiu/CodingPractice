#Time: O(v/n), n is the total amount of integer, v is vectors, the total is (n+v)/n 
#Space: O(1)
class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.vector = v
        self.x = 0
        self.y = 0
        

    def next(self) -> int:
        while self.x < len(self.vector) and self.y == len(self.vector[self.x]):
            self.x+=1
            self.y=0
        ret = self.vector[self.x][self.y]
        self.y+=1
        return ret
        

    def hasNext(self) -> bool:
        while self.x < len(self.vector) and self.y == len(self.vector[self.x]):
            self.x+=1
            self.y=0
        return self.x < len(self.vector)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()