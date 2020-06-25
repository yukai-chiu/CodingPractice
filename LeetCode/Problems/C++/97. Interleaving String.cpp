class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        if(s3.size() != s1.size()+s2.size()) return false;
        
        int M = s1.size()+1;
        int N = s2.size()+1;
        
        bool * dp = new bool[M*N]{};

        for(int i=0;i<M;i++){
            for(int j=0;j<N;j++){
                if(i==0 && j == 0)
                    dp[i*N+j] = true;
                else if(i==0)
                    dp[i*N+j] = dp[i*N+j-1] && (s2[j-1] == s3[i+j-1]);
                else if(j==0)
                    dp[i*N+j] = dp[(i-1)*N+j] && (s1[i-1] == s3[i+j-1]);
                else
                    dp[i*N+j] = (dp[i*N+j-1] && (s2[j-1] == s3[i+j-1])) or dp[(i-1)*N+j] && (s1[i-1] == s3[i+j-1]);
            }
        }
        return dp[M*N-1];
    }
};