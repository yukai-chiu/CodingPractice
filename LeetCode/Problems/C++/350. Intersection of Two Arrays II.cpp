class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        if(!nums1.size() || !nums2.size()) return {};
        
        vector<int> result;
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
       
        int pt1 = 0;
        int pt2 = 0;
        int left, right;
        
        while(pt1 < nums1.size() && pt2 < nums2.size()) {
            left = nums1[pt1];
            right = nums2[pt2];
            if(left == right){
                result.push_back(left);
                pt1++;
                pt2++;
                continue;
            }
            else if(left < right)
                while(pt1< nums1.size() && left == nums1[pt1]) pt1++;
            else
                while(pt2 < nums2.size() && right == nums2[pt2]) pt2++;
        }
        return result;
    }
};