"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        #Time: O(n), traverse all the nodes 
        #Space: O(1)

        if not root:
            return root

        leftmost = root
        
        #keep track of the left most node inorder to traverse to the end of the level
        while leftmost:
            #we can use the parent ptr to iterate through the level since it's already been set
            parent = leftmost
            leftmost = None
            prev = None
            while parent:
                #if left child exists, we can do the follow
                # 1. Complete the prev ptr and point "prev.next" to it
                # 2. set the prev ptr with left child
                # 
                if parent.left:
                    if prev:
                        prev.next = parent.left 
                    prev = parent.left
                    #keep track of the leftmost node of the next level
                    if not leftmost:
                        leftmost = parent.left
                        
                #if right child exists, we can do the follow
                # 1. Complete the prev ptr and point "prev.next" to it
                # 2. set the prev ptr with right child
                #         
                if parent.right:
                    if prev:
                        prev.next = parent.right
                    prev = parent.right
                    if not leftmost:
                        #keep track of the leftmost node of the next level
                        leftmost = parent.right
 
                #move parent to right in the level
                parent = parent.next


        return root