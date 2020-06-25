class RandomizedSet {
public:
    vector<int> lookup;
    unordered_map<int, int> mydata;
    /** Initialize your data structure here. */
    RandomizedSet() {
        lookup = {};
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(mydata.find(val) == mydata.end()){
            mydata[val] = lookup.size();
            lookup.push_back(val);
            return true;
            }
        else
            return false;

    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if(mydata.find(val) == mydata.end())
            return false;
        else{
            int idx = mydata[val];
            int last = lookup.back();
            mydata[last] = idx;
            lookup[idx] = last;
            lookup.pop_back();
            mydata.erase(val);
            
            return true;
        }
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        int r = rand() % mydata.size();
        return lookup[r];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */