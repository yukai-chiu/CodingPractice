//Time: O(n)
//Space:O(n)
class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        if(!A.size()) return -1;
        
        unordered_set<int> unique;
        for(int a:A){
            if(unique.find(a)!= unique.end()) return a;
            unique.insert(a);
            
        }
        return -1;
    }
};

//Time: O(n)
//Space:O(1)
class Solution {
public:
    int repeatedNTimes(vector<int>& A) {
        if(!A.size()) return -1;
        
        for(int k=1;k<=3;k++)
            for(int i=0;i<A.size()-k;i++)
                if(A[i] == A[i+k]) 
                    return A[i];
        
        return -1;
    }
};