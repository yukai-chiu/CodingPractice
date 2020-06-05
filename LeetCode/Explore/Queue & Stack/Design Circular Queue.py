class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [-1] * k
        self.head = -1
        self.tail = -1
        self.size = k
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        #case full
        if self.isFull():
            return False
        
        #case empty
        elif self.isEmpty():
            self.head = 0
            
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
       
        return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self.tail == self.head:
            self.head = -1
            self.tail = -1
            return True
        
        self.head = (self.head +1) % self.size
            
        return True
        
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.queue[self.head]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.tail == -1 and self.head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return ((self.tail + 1) % self.size) == self.head
       
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()