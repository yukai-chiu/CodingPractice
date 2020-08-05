class Solution {
public:
    int trap(vector<int>& height) {
        if(!height.size()) return 0;
        int trapped_water = 0;
        int l = 0, r = height.size()-1;
        int l_max = height.front();
        int r_max = height.back();
        
        
        while(l <= r){
            //move from the smaller side
            if(height[l] < height[r]){
                l_max = max(l_max, height[l]);
                trapped_water+= l_max - height[l];
                l++;
            }
            else{
                r_max = max(r_max, height[r]);
                trapped_water+= r_max - height[r];
                r--;
            }
        }
        return trapped_water;
    }
};