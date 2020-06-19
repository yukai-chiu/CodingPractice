//binary search
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        if(!A.size()) return -1;
        int N = A.size();
        int l = 0, r = N-1;
        
        while(l<r){
            int mid = l + (r-l)/2;
            if(A[mid]<A[mid+1]){
                l = mid+1;
            }
            else{
                r = mid;
            }
        }
        //cout << l << r;
        return r;
    }
};

//linear search
lass Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        if(!A.size()) return -1;
        
        for(int i=0;i<A.size();i++){
            if(A[i]>A[i+1]){
                return i;
            }
        }
        return 0;
    }
};