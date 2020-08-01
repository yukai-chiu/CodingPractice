class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if not N:
            return 0

        count = 0
        #N = (x+1) + (x+2) + .... + (x+k)
        #N = xk + k(k+1)/2
        #x should be greater than 0
        #N >= k(k+1)/2
        #2N >= k(k+1)
        #2N + 1/4 >= (k+1/2)^2
        #sqrt(2N+1/4) >= k+1/2
        #sqrt(2N+1/4) - 1/2 >= k
        #we know the upper bound of k
        for k in range(1,ceil(sqrt(2*N+0.25)-0.5)+1):
            #match x requirement
            #1. x >=0
            #2. x is integer
            if (N - (k*(k+1)//2)) % k == 0:
                count+=1
        
        return count