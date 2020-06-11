#Heap
#Time: O(nlogk)
#Space: O(k) 
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        heap = []
        
        #initialize
        for i in range(len(lists)):
            if lists[i] is not None:
                #adding i in the middle as a tie breaker
                #if the value is the same, heap cannot compare listNode
                #so we put the index in the middle to solve it
                heapq.heappush(heap,(lists[i].val, i, lists[i]))
        head = ListNode(0)
        curr = head
        #length = len(lists)
        i = 0
        #iterate
        while heap:
            #is we don't change the size of the heap,
            #it is faster using heapreplace
            #we only pop it when necessary
            val, i, node = heap[0]#heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            if node is not None:
                heapq.heapreplace(heap,(node.val, i, node))
            else:
                heapq.heappop(heap)


        return head.next