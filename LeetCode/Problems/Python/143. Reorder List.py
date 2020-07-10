#Time: O(n)
#Space: O(1)
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        fast = head
        slow = head
        #reverse the right part of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
                  
        #after this, l.next will be the first node of the list to be reverse
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        #we'll get prev as the head of the reversed list
        first = head
        second = prev
        while second:
            temp = first.next
            first.next = second
            second = second.next
            first.next.next = temp
            first = temp