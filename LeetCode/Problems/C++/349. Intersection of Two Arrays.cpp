//hash set
//Time: O(m+n)
//Space: O(m+n)
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        if(!nums1.size() || !nums2.size()) return {};
        
        vector<int> result;
        unordered_set<int> unique_1;
        unordered_set<int> unique_2;
        if(nums1.size() > nums2.size()){
            vector<int> temp = nums1;
            nums1 = nums2;
            nums2 = temp;
        }
        
        for(int i=0;i<nums1.size();i++)
            unique_1.insert(nums1[i]);
        for(int i=0;i<nums2.size();i++)
            unique_2.insert(nums2[i]);
        
        for(auto it=unique_1.begin();it!=unique_1.end();it++){
            if(unique_2.find(*it)!= unique_2.end())
                result.push_back(*it);
        }
        
        return result;
    }
};

//sorting
//Time: O(mlogm + nlogn)
//Space: O(1)
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
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
                while(pt1< nums1.size() && left == nums1[pt1]) pt1++;
                while(pt2 < nums2.size() && right == nums2[pt2]) pt2++;
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


class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        if(!nums1.size() || !nums2.size()) return {};
        
        vector<int> result;
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
       
        int pt1 = 0;
        int pt2 = 0;
        
        while(pt1 < nums1.size() && pt2 < nums2.size()) {
            if(nums1[pt1] == nums2[pt2]){
                result.push_back(nums1[pt1]);
                pt1++;
                pt2++;
            }
            else if(nums1[pt1] < nums2[pt2])
                pt1++;
            else
                pt2++;
            
            while(pt1 < nums1.size() && pt1 > 0 && nums1[pt1] == nums1[pt1-1])
                pt1++;
            while(pt2 < nums2.size() && pt2 > 0 && nums2[pt2] == nums2[pt2-1])
                pt2++;
        }

        return result;
    }
};