class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        if(!rectangles.size()) return false;
        
        int N = rectangles.size();
        int min_x = INT_MAX, min_y = INT_MAX;
        int max_x = INT_MIN, max_y = INT_MIN;
        unordered_set<string> nodes;
        int max_area = 0;
        int sum_area = 0;
        string p = "";
        vector<pair<int, int>> corner = {{0,1}, {0,3}, {2,1}, {2,3}};
        
        for(int i=0;i<N;i++){
            
            int area = (rectangles[i][2] - rectangles[i][0]) * (rectangles[i][3] - rectangles[i][1]);
            
            for(int j=0;j<4;j++){
                p = "";
                p.append(to_string(rectangles[i][corner[j].first]));
                p.append(to_string(rectangles[i][corner[j].second]));
                if(nodes.find(p) == nodes.end()) nodes.insert(p);
                else nodes.erase(p);
            }

            min_x = min(min_x, rectangles[i][0]);
            min_y = min(min_y, rectangles[i][1]);
            max_x = max(max_x, rectangles[i][2]);
            max_y = max(max_y, rectangles[i][3]);
            sum_area += area;
            
        }
        max_area = (max_x - min_x) * (max_y - min_y);

        if(sum_area != max_area) return false;
        
        p = "";
        p.append(to_string(min_x));
        p.append(to_string(min_y));
        if(nodes.find(p) == nodes.end()) return false;
        
        p = "";
        p.append(to_string(max_x));
        p.append(to_string(min_y));
        if(nodes.find(p) == nodes.end()) return false;
        
        p = "";
        p.append(to_string(min_x));
        p.append(to_string(max_y));
        if(nodes.find(p) == nodes.end()) return false;
        
        p = "";
        p.append(to_string(max_x));
        p.append(to_string(max_y));
        if(nodes.find(p) == nodes.end()) return false;
        
        if(nodes.size() != 4) return false;
        
        return true;
    }
};