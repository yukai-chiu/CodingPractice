class MyCircularDeque {
private:
    int capacity;
    int count;
    vector<int> myqueue;
    int front;
    int rear;
    
public:
    /** Initialize your data structure here. Set the size of the deque to be k. */
    MyCircularDeque(int k) {
        count = 0;
        capacity = k;
        myqueue.resize(k);
        front = k-1;
        rear = 0;
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    bool insertFront(int value) {
        if(isFull()) return false;
        
        myqueue[front] = value;
        front = (front+capacity-1) % capacity;
        count++; 
        return true;
    }
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    bool insertLast(int value) {
        if(isFull()) return false;
        myqueue[rear] = value;
        rear = (rear+1) % capacity;
        count++;
        return true;
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    bool deleteFront() {
        if(isEmpty()) return false;
        front = (front+1) % capacity;
        count--;
        return true;
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    bool deleteLast() {
        if(isEmpty()) return false;
        rear = (rear +capacity-1) % capacity;
        count--;
        return true;
    }
    
    /** Get the front item from the deque. */
    int getFront() {
        return isEmpty() ?  -1 : myqueue[(front+1)%capacity];
    }
    
    /** Get the last item from the deque. */
    int getRear() {
        return isEmpty() ? -1 : myqueue[(rear+capacity-1)%capacity];
    }
    
    /** Checks whether the circular deque is empty or not. */
    bool isEmpty() {
        return count==0;
    }
    
    /** Checks whether the circular deque is full or not. */
    bool isFull() {
        return count == capacity;
    }
};