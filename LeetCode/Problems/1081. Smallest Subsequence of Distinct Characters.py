#Time: O(n)
#Space: O(n)
class Solution:
    def smallestSubsequence(self, text: str) -> str: 
        #intuition:
        #if we want the smallest lexicographical subsequence
        #the larger character should be at the back
        #unless there's no more at the back and they have to be in the front
        #so what we really want is to remove all duplicated char and make is smallest
        
        
        if not text:
            return text
        
        #first we are going to check the last index for every distinct char
        last = {}
        
        for i, t in enumerate(text):
            last[t] = i
        
        #next we are going to use a stack to check from the start
        stack = []
        #if 
        #1. stack is empty, we push the current
        #2. while the current is smaller than  stack[-1], we check if we can find stack[-1] later
        #   if yes, we pop it.
        #3. also we want to make sure that there's only 1 in stack for each distinct char
        #   so we can use a set for faster check of this 
        #   after we pop it, we have to remove from seen
        seen = set()
        
        for i, t in enumerate(text):
            if t not in seen:
                while stack and t < stack[-1] and last[stack[-1]] > i:
                    seen.discard(stack.pop())
                stack.append(t)
                seen.add(t)
        return "".join(stack)
                
        
        
        
        
        return