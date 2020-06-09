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
       


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return ListNode(0)
        #if one of them is None
        #return the other
        if not l1:
            return l2
        if not l2:
            return l1
        
        carry = 0
        root = ListNode(None)
        curr = root
        while l1 and l2:
            temp = l1.val + l2.val + carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp-=10
            curr.next = ListNode(temp)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            temp = l1.val + carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp-=10
            curr.next = ListNode(temp)
            curr = curr.next
            l1 = l1.next
        
        while l2:
            temp = l2.val + carry
            carry = 0
            if temp >= 10:
                carry = 1
                temp-=10
            curr.next = ListNode(temp)
            curr = curr.next
            l2 = l2.next
        
        if carry ==1:
            curr.next = ListNode(1)
        
        return root.next
        
        #we can iterate through two linked list and use a carry to calculate