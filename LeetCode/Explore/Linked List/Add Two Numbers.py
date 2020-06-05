# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Old implementation
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0

        
        head = ListNode(0) 
        current_node = head
        while(l1 and l2):
            carry, r = divmod(l1.val + l2.val + carry, 10)
            current_node.val = r
            l1 = l1.next
            l2 = l2.next
            if(l1 and l2):
                current_node.next = ListNode(0)
                current_node = current_node.next
        while(l1):
            current_node.next = ListNode(0)
            current_node = current_node.next
            carry, r = divmod(l1.val + carry, 10)
            l1 = l1.next
            current_node.val = r
            
        
        while(l2):
            current_node.next = ListNode(0)
            current_node = current_node.next
            carry, r = divmod(l2.val + carry, 10)
            l2 = l2.next
            current_node.val = r
        
        if(carry == 1):
            current_node.next = ListNode(1)

        return head   
       