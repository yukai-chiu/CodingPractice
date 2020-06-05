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