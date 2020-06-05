"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

#solution 1
#bfs
class Solution:
    def connect(self, root: 'Node') -> 'Node':
         
        #Time: O(n), traverse all the nodes 
        #Space: O(n), the last layer of full binary tree contains n/2 nodes
        
        if not root:
            return root
        
        queue = [root]
        
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.pop(0)      
                if i < size - 1:
                    curr.next = queue[0]

                if curr.left and curr.right:
                    queue.append(curr.left)
                    queue.append(curr.right)
        
        return root
                    

#solution 2
#Using previously established next pointers
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        #Time: O(n), traverse all the nodes 
        #Space: O(1)
        
        if not root:
            return root
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            while head:
                #case 1
                head.left.next = head.right
                #case 2
                if head.next:
                    head.right.next = head.next.left
                #move right
                head = head.next
            #go to the next level 
            leftmost = leftmost.left
        
        return root
                            