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