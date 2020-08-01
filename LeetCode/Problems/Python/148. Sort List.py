#merge sort
#Time: O(nlogn)
#Space: O(logn)
class Solution:
    def mergeSort(self, head):
        if head.next:
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            temp = slow.next
            slow.next = None
            
            left = self.mergeSort(head)
            right = self.mergeSort(temp)
            if not right:
                return left
            if not left:
                return right

            if left.val <= right.val:
                node = left
                left = left.next
            elif left.val > right.val:
                node = right
                right = right.next
            merge = node
            
                                
            while left and right:
       
                if left.val < right.val:
                    merge.next = left
                    left = left.next
                else:
                    merge.next = right
                    right = right.next
                merge = merge.next

            while left:
                merge.next = left
                left = left.next
                merge = merge.next
            while right:
                merge.next = right
                right = right.next
                merge = merge.next
            return node
        return head
        
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return self.mergeSort(head)
        
        