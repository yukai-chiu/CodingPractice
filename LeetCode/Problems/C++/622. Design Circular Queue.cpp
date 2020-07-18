//Array
class MyCircularQueue {
private:
    int count;
    vector<int> myqueue;
    int capacity;
    int front;
    int rear;
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        myqueue.resize(k);
        capacity = k;
        count = 0;
        front = 0;
        rear = 0;
        
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if(isFull()) return false;
        rear = (front+count) % capacity;
        myqueue[rear] = value;
        count++;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if(isEmpty()) return false;       
        count--;
        front = (front+1)%capacity;
        return true;
    }
    
    /** Get the front item from the queue. */
    int Front() {
        if(isEmpty()) return -1;
        return myqueue[front];
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        if(isEmpty()) return -1;
        return myqueue[rear];
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return count == 0;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return count == capacity;
    }
};
class LinkNode {
    public:
        int val;
        LinkNode* next;
        LinkNode(int value){
            val = value;
            next = NULL;
        }
};

//Linked List
class MyCircularQueue {
private:
    int count;
    LinkNode* head;
    int capacity;
    int front;
    LinkNode* rear;
public:
    /** Initialize your data structure here. Set the size of the queue to be k. */
    MyCircularQueue(int k) {
        head = NULL;
        capacity = k;
        count = 0;
        front = 0;
        rear = head;
        
    }
    
    /** Insert an element into the circular queue. Return true if the operation is successful. */
    bool enQueue(int value) {
        if(isFull()) return false;
        LinkNode* new_node = new LinkNode(value);
        if(isEmpty()){
            head = new_node;
            rear = new_node;
        }
        else{
            rear->next = new_node;
            rear = rear->next;
        }
        count++;
        return true;
    }
    
    /** Delete an element from the circular queue. Return true if the operation is successful. */
    bool deQueue() {
        if(isEmpty()) return false;       
        count--;
        rear->next = head->next;
        head = head->next;
        
        return true;
    }
    
    /** Get the front item from the queue. */
    int Front() {
        if(isEmpty()) return -1;
        return head->val;
    }
    
    /** Get the last item from the queue. */
    int Rear() {
        if(isEmpty()) return -1;
        return rear->val;
    }
    
    /** Checks whether the circular queue is empty or not. */
    bool isEmpty() {
        return count == 0;
    }
    
    /** Checks whether the circular queue is full or not. */
    bool isFull() {
        return count == capacity;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
 */