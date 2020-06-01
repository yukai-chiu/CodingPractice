class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #brute force:
        #generate all possibilities and check each of them
        #Time: O(2^n) since every index will have 2 possibility
        
        #can we do better?
        #maybe use a tree structure and stack
        #we want to find the valid path with length or 6
        #it should be balanced, if we say "(" --> +1, ")" --> -1. on the way of path, 
        #balance shuold never be smaller than 0
        #when we made decision, balance should always be smaller than n/2 and n-i, since we want it to end at 0.
        #we can use BFS to traverse the tree
        if not n:
            return []
        
        deq = collections.deque()
        deq.append((1,1,"("))
        result = set()
        target = 2 * n
        while deq:
            length, balance, para = deq.popleft()
            if length < target:
                length +=1
                if balance < target - length:
                    deq.append((length,balance+1, para +"("))
                if balance > 0:
                    deq.append((length,balance-1, para +")"))

            elif length == target:
                result.add(para)
        return result

#clear method
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        
        deq = collections.deque()
        deq.append((1,0,"("))
        result = []
        while deq:
            left,right, para = deq.popleft()
            if len(para) < 2*n:
                if left < n:
                    deq.append((left+1,right, para +"("))
                if left > right:
                    deq.append((left,right+1, para +")"))
            else:
                result.append(para)
        return result