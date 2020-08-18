struct LinkedNode {
    int key;
    int val;
    LinkedNode* next;
    LinkedNode(int _key, int _val){
        key = _key;
        val = _val;
        next = nullptr;
    }
};

class MyHashMap {
private:
    vector<LinkedNode*> hashmap;
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        hashmap.resize(2069);
        for(int i=0;i<hashmap.size();i++){
            hashmap[i] = new LinkedNode(-1, -1);
        }
    
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int index = key%2069;

        LinkedNode* curr = hashmap[index];
        while(curr->next!=NULL){
            if(curr->next->key == key){
                curr->next->val = value;
                return;
            }
            curr = curr->next;
        }
        curr->next = new LinkedNode(key, value);
        
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int index = key%2069;
        
        LinkedNode* curr = hashmap[index]->next;
        while(curr!=NULL){
            if(curr->key == key) return curr-> val;
            curr = curr->next;
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int index = key%2069;
        LinkedNode* curr = hashmap[index];
        while(curr->next!=NULL){
            if(curr->next->key == key){
                LinkedNode* temp = curr->next;
                curr->next = curr->next->next;
                delete temp;
                break;
            }
            curr = curr->next;
        }
          
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */