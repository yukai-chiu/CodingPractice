class Solution:
    def numSquares(self, n: int) -> int:
        if not n:
            return 0
        if n < 2:
            return n
        
        queue = [n]
        num = 0
        
        sqs = []
        i = 1
        while i*i <= n:
            sqs.append(i * i)
            i+=1
        seen = {}
        while queue:
            num += 1
            temp = set()
            for i in range(len(queue)):
                curr = queue.pop(0)
                for s in sqs:
                    if curr == s:
                        return num     
                    #add remainer, use set to remove duplicates
                    temp.add(curr - s)
            queue.extend(temp)

                