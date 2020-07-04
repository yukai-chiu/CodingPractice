# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        slow = head
        fast = head
        step = 0
        while fast:
            if step % 2 == 1:
                slow = slow.next
            fast = fast.next
            step+=1
        
        return slow