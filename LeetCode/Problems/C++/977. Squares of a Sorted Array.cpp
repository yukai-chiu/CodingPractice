class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        
        //we can calculate all the result and sort it later
        //but we can also do the following to optimize the time complexity
        //find the pivot, and use two pointers
        for(int i=0;i<A.size();i++){
            A[i] *= A[i];
        }
        sort(A.begin(),A.end());
        return A;
    }
};



class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        
        if(!A.size()) return {};
        int r = 0, l;
        vector<int> ans;
        while(r < A.size() && A[r]<0){
            r++;
        }
        
        l = r -1;

        while(l >=0 && r < A.size()){
            if(abs(A[l]) < abs(A[r])) {
                
                ans.push_back(A[l] * A[l]);
                l--;
            }
            else{
                ans.push_back(A[r] * A[r]);
                r++;
            }
        }
        while(l >=0){
            ans.push_back(A[l] * A[l]);
            l--;
        }
        
        while(r < A.size()){
            ans.push_back(A[r] * A[r]);
            r++;
        }
        return ans;
    }
};