#DPS + Memo
class Solution:
    """
    @param n: the number of people
    @param m: the number of groups
    @return: the number of grouping options
    """
    
    def groupingOptions(self, n, m):
        # write your code here
        #dfs + memo
        #dp
        #run a for loop and separate
        #the loop will go up to n/m 
        #base case
        #if there's only one group
        #we put all the ppl in the group
        def groupHelper(n,m,threshold, memo):
            if m == 1:
                    return 1
            
            if (n,m,threshold) in memo:
                return memo[(n,m,threshold )]
            count = 0
            for i in range(threshold, (n//m)+1):
                #get the group first
                #and we modify to count number later
                #print(i,(n//m)+1,n-i,m-1)
                groups = groupHelper(n-i,m-1,i, memo)
                count+= groups
                    
            #print("count:", n,m,count)
            memo[(n,m,threshold)] = count
            return memo[(n,m,threshold)]
            
        memo = {}    
        ans = groupHelper(n,m,1, memo)   
        print(memo)
        return ans

#DP
class Solution:
    """
    @param n: the number of people
    @param m: the number of groups
    @return: the number of grouping options
    """
    
    def groupingOptions(self, n, m):
        if n < m:
            return 0
            
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        #dp[i][j] means how many options to group i ppl in j groups
        #so we can initial the j=0 column with all 1
        for i in range(n+1):
            dp[i][1] = 1
        
        #next if n = m, there's only one option to put 1 ppl in each group
        #in fact this is also the upright bound of the matrix
        for j in range(1,m+1):
            dp[j][j] = 1
            
        #next, the idea is a bit tricky from here
        #if we have i people and we want to form j groups
        #we can first give all j groups 1 ppl
        #the remaining will be i-j ppl
        #we can now sum up all the options of "(i-j) ppl in 1 group, (i-j) ppl in 2 group......(i-j) ppl in j group"
        #which is the previous row that we already computed 
        #we can build up the array this way
        
        #we already finished i = 0 and 1
        for i in range(2,n+1):
            #we don't need to go to the up right array since we are bounded by i=j
            #so the bound here will be i or m
            #we alreay finish j = 0
            for j in range(2,min(i,m+1)):
                for k in range(j+1):
                    dp[i][j] += dp[i-j][k]
                    
        
        
        #print(dp)
        return dp[n][m]