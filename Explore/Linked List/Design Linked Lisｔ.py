#My first try
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        temp = ListNode(val)
        temp.next = self.head
        
        self.head = temp
        self.length +=1
        print(self.head.val)
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        self.length+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        if index == 0:
            temp = self.head
            self.head = ListNode(val)
            self.head.next = temp
            print(self.head.val)
            self.length+=1
            return
        prev = ListNode(None)
        prev.next = self.head
        curr = self.head
        for i in range(index):
            curr = curr.next
            prev = prev.next
        
        temp = ListNode(val)
        prev.next = temp
        temp.next = curr
        print(prev.val)
        self.length+=1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length-=1
            return
        
        prev = ListNode(None)
        prev.next = self.head
        curr = self.head
        for i in range(index):
            curr = curr.next
            prev = prev.next
        
        if curr:
            prev.next = curr.next
        else:
            prev.next = None

        
        self.length-=1