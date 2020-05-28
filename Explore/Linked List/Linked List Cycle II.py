# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Hash map
#Time: O(n)
#Space: O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        hash_map = {}
        while head:
            if head.next in hash_map:
                return head.next
            elif head not in hash_map:
                hash_map[head] = True
            head = head.next
        return None