# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Hashmap
#Time: O(n)
#Space: O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        hash_map = {}
        while head:
            if head not in hash_map:
                hash_map[head] = True
            else:
                return True
            head = head.next
        return False


#Two pointer
#Time: O(n+k), n = all the nodes, k = cyclic range
#Space: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        fast = head.next
        slow = head
        step = 0
        while fast:
            if step % 2 ==1:
                slow = slow.next
            if fast==slow:
                return True
            fast = fast.next
            print(fast)
            step+=1

        return False