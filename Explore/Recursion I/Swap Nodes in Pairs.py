# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Recursive
#Time: O(n)
#Space: O(n)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
                return head
        
        first = head
        second = head.next

        first.next = self.swapPairs(head.next.next)
        second.next = first
        
        return second


#Iterative
#Time: O(n)
#Space: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
                return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            
            first = head
            second = head.next
            #swap
            first.next = second.next
            second.next = first 
            #connect to prev node
            prev.next = second
            #update for the next round
            head = first.next
            prev = first
      
        
        return dummy.next
        
        
                
                

