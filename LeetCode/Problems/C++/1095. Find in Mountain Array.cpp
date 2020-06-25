/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int l = 0;
        int r = mountainArr.length()-1;
        int mid;
        
        //find peak
        while(l<r){
            mid = l + (r-l)/2;
            if(mountainArr.get(mid)>mountainArr.get(mid+1))
                r = mid;
            else
                l = mid+1;
        }
        
        int pivot = l;
        
        l = 0;
        r = pivot;
        
        //search in left
        while(l<=r){
            mid = l + (r-l)/2;
            if(mountainArr.get(mid) == target) 
                return mid;
            else if(mountainArr.get(mid) < target)
                l = mid+1;
            else
                r = mid-1;
        }
        
        //search in right
        l = pivot+1;
        r = mountainArr.length()-1;
        
        while(l<=r){
            mid = l + (r-l)/2;
            if(mountainArr.get(mid) == target) 
                return mid;
            else if(mountainArr.get(mid) < target)
                r = mid-1;
            else
                l = mid+1;
        }
        
        
        
        
        return -1;
    }
};