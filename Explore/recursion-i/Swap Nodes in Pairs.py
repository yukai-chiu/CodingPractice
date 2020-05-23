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