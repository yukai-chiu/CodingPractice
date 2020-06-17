struct DLinkedNode {
    int val;
    int key;
    DLinkedNode* prev;
    DLinkedNode* next;
    DLinkedNode(){
        val = 0;
        key = 0;
        prev = NULL;
        next = NULL;
    }
    
};
class LRUCache {
private:
    int _capacity;
    int _size;
    unordered_map<int, DLinkedNode*> cache;
    DLinkedNode* head;
    DLinkedNode* tail;
    
    
    void addNode(DLinkedNode* node){
        //handle node
        node->prev = head;
        node->next = head->next;
        //handle head
        head->next->prev = node;
        head->next = node;
    }
    
    void removeNode(DLinkedNode* node){
        //handle node
        node->prev->next = node->next;
        //handle tail
        node->next->prev = node->prev;
    }
    
    
    
public:
    LRUCache(int capacity) {
        _capacity = capacity;
        _size = 0;
        head = new DLinkedNode();
        tail = new DLinkedNode();
        head->next = tail;
        tail->prev = head;
        
    }
    
    int get(int key) {
        if(cache.find(key) == cache.end()){
            return -1;
        }
        DLinkedNode* node = cache[key];
        removeNode(node);
        addNode(node);
        
        return node->val;
        
    }
    
    void put(int key, int value) {
        if(cache.find(key) == cache.end()){
            DLinkedNode* node = new DLinkedNode();
            node->key = key;
            node->val = value;
            cache[key] = node;
            addNode(node);
            _size++;
            
            if(_size > _capacity){
                DLinkedNode* to_pop = tail->prev;
                removeNode(to_pop);
                cache.erase(to_pop->key);
                _size--;
            }
            
        }
        else{
            DLinkedNode* node = cache[key];
            node->val = value;
            removeNode(node);
            addNode(node);
        }
    }
    
    
};