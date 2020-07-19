class Vector2D {
public:
    Vector2D(vector<vector<int>>& v) {
        my_vector = &v;
        x = 0;
        y = 0;
    }
    
    int next() {
        hasNext();
        return (*my_vector)[y][x++];
    }
    
    bool hasNext() {
        
        while(y<my_vector->size() && x==(*my_vector)[y].size()){
            x=0;
            y++;
        }
        return y<my_vector->size();
    }
private:
    int x, y;
    vector<vector<int>>* my_vector;
};


class Vector2D {
public:
    Vector2D(vector<vector<int>>& v) {
        it = v.begin();
        end = v.end();
        x = 0;
       
    }
    
    int next() {
        hasNext();
        return (*it)[x++];
    }
    
    bool hasNext() {
        
        while(it!=end && x==(*it).size()){
            x=0;
            it++;
        }
        return it!=end;
    }
private:
    int x;
    vector<vector<int>>::iterator it, end;
};
