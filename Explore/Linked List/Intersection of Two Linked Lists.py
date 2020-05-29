#Brute Force
#Time limit exceed
#Time: O(m*n)
#Space: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        while headA:
            curr = headB
            while curr:
                if curr ==headA:
                    #print(headA,curr)
                    return curr
                curr = curr.next
            headA = headA.next
        return None

#Hash table
#Time: O(n)
#Space: O(n)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #finish traverse headA first, and add each into hash table
        #start from headB, if it any of the node in hash table, return
        #if also finish headB, means no intersection, return None
        #Time: O(n), Space: O(n)
        if not headA or not headB:
            return None
        
        hash_table = {}
        
        #Construct hash table
        while headA:
            hash_table[headA] = True
            headA = headA.next
        while headB:
            if headB in hash_table:
                return headB
            headB = headB.next
        return None

#Two pointers
#Time: O(m+n)
#Space: O(1)
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #if the first one finish, connect to another head
        #This is because two pointers will traverse the same amount
        #Which means they will end together
        #we only need to see if they eventually pointed at the same node
        #If it's not the same node at the end, there's not intersection
        if not headA or not headB:
            return None
        p1 = headA
        p2 = headB
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            
            if p1 == None:
                p1 = headB
            elif p2 == None:
                p2 = headA
                
        return None