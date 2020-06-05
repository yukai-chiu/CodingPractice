# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Old implementation
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        l_ptr = dummy
        r_ptr = dummy      
       
        for i in range(n+1):
            r_ptr = r_ptr.next
        
        
        
        while(r_ptr):
            l_ptr = l_ptr.next
            r_ptr = r_ptr.next

        l_ptr.next = l_ptr.next.next
        
        
        return dummy.next


#Two pass
#Time: O(n)
#Space: O(1)
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #Intuition: we need to know the length of the linked list, so that we know which to remove
        #If we traverse it once, we can locate it
        #Use two pointers and keep the distance between them as n? So if the fast pointer reaches the end,
        #we know the slow pointer is the one we want to remove
        if not head:
            return None
        
        length = 0
        curr = head
        while curr:
            length +=1
            curr = curr.next
        print(length)
        
        sentinel = ListNode(0)
        sentinel.next = head
        curr = sentinel
        target = length - n
        for i in range(target):
            curr = curr.next
        curr.next = curr.next.next
        
        return sentinel.next

#Two pointer
#One pass
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #Intuition: we need to know the length of the linked list, so that we know which to remove
        #If we traverse it once, we can locate it
        #Use two pointers and keep the distance between them as n? So if the fast pointer reaches the end,
        #we know the slow pointer is the one we want to remove
        if not head:
            return None
        
        
        sentinel = ListNode(0)
        sentinel.next = head
        prev, curr = sentinel, head
        for i in range(n):
            curr = curr.next
        while curr:
            curr = curr.next
            prev = prev.next

        prev.next = prev.next.next
        
        return sentinel.next