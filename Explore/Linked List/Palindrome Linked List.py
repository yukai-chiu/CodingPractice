# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #Brute force 1
        #1. store the str of the linked list
        #2. iterative check the palindrome 
        if not head:
            return True
        
        array = []
        
        while head:
            array.append(head.val)
            head = head.next
        
        for i in range(len(array)//2):
            if array[i] != array[-1-i]:
                return False
        return True
        
        #Brute force 2
        #reverse the whole linked list and compare with forward traverse
        
        #Optimized?
        #Intuition: get the length first --> use two pointer to get 
        #find the pivot, and reverse half of the linked list
        #Two cases, even and odd
        #compare each node, if it doesn't match, return False
        #if reach the end, return True
        
        