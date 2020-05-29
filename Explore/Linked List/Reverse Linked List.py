# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Old Implementation
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        end = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return end
       



#Recursive
#Time: O(2L) => O(L)
#Space: O(L), L = length of the linked list
class Solution:
    def recursiveHelper(self, node):
        if not node.next:
            return node
        head_ref = self.recursiveHelper(node.next)
        node.next.next = node
        node.next = None
        return head_ref
    
    def reverseList(self, head: ListNode) -> ListNode:
        #Intuition:
        #Recusively traverse all the way to the end
        #each round let the returned node.next set to current
        #use two pointer? 
        #one point to end all the time for final result
        #one to set up the link
        #every time need to set next to None first so there won't be cycle
        
        if not head:
            return None
        reversed_ans = self.recursiveHelper(head)
        
        return reversed_ans

#Iterative
#Time: O(n)
#Space: O(1)
class Solution:
    
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        curr = head
        prev = None
        while curr:
            
            temp = curr.next
            curr.next = prev           
            #set for next iteration
            prev = curr
            curr = temp

        return prev
        
        
        