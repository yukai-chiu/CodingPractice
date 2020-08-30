class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        if(!rectangles.size()) return false;
        
        unordered_set<string> points;
      
        int min_x = INT_MAX;
        int min_y = INT_MAX;
        int max_x = INT_MIN;
        int max_y = INT_MIN;
        int area= 0;
        vector<pair<int,int>> corner{{0,1},{2,3},{2,1},{0,3}};
        
        for(int i=0;i<rectangles.size();i++){
            for(int j=0;j<4;j++){
                string temp = "";
                temp += to_string(rectangles[i][corner[j].first]);
                temp +=',';
                temp += to_string(rectangles[i][corner[j].second]);
                
                if(points.find(temp)==points.end())
                    points.insert(temp);
                else
                    points.erase(temp);
            }
            area+= (rectangles[i][2] - rectangles[i][0])*(rectangles[i][3] - rectangles[i][1]);
            min_x = min(min_x, rectangles[i][0]);
            min_y = min(min_y, rectangles[i][1]);
            max_x = max(max_x, rectangles[i][2]);
            max_y = max(max_y, rectangles[i][3]);
        }
        
        if (area != (max_x-min_x)*(max_y-min_y)) return false;
        
        if(points.size() != 4) return false;
        
        if(points.find(to_string(min_x)+','+to_string(min_y))==points.end())
            return false;
        if(points.find(to_string(min_x)+','+to_string(max_y))==points.end())
            return false;
        if(points.find(to_string(max_x)+','+to_string(min_y))==points.end())
            return false;
        if(points.find(to_string(max_x)+','+to_string(max_y))==points.end())
            return false;
       
        
        

        return true;
    }
};


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