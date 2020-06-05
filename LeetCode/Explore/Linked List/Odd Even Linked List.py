# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#First try: Two pointer
#Time: O(node)
#Space: O(1)
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #use two pointer, one traverse odd, one traverse even
        #when both are None, connect the odd with the head of even 
        if not head or not head.next:
            return head
        
        p1 = odd = head
        p2 = even = head.next
        #print(p1,p2)
        while p1.next and p2.next:
            #print(p1.val,p2.val)
            if p1 and p1.next:
                p1.next = p1.next.next
                p1 = p1.next
            if p2 and p2.next:
                p2.next = p2.next.next
                p2 = p2.next
        #print(p1,p2)
        p1.next = even
        return odd
        

#Polished version
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #use two pointer, one traverse odd, one traverse even
        #when both are None, connect the odd with the head of even 
        if not head :
            return head
        
        p1 = head
        p2 = even = head.next

        while p2 and p2.next:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next

        p1.next = even
        return head