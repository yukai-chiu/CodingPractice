/*
 * Below is the interface for Iterator, which is already defined for you.
 * **DO NOT** modify the interface for Iterator.
 *
 *  class Iterator {
 *		struct Data;
 * 		Data* data;
 *		Iterator(const vector<int>& nums);
 * 		Iterator(const Iterator& iter);
 *
 * 		// Returns the next element in the iteration.
 *		int next();
 *
 *		// Returns true if the iteration has more elements.
 *		bool hasNext() const;
 *	};
 */

class PeekingIterator : public Iterator {
public:
    int peekedNext;
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.
	    peekedNext = INT_MIN;
        ;
	}
	
    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        if(peekedNext!= INT_MIN)
            return peekedNext;
        else{
            peekedNext = Iterator::next();
            return peekedNext;
        }
	}
	
	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    if(peekedNext!= INT_MIN){
            int ret = peekedNext;
            peekedNext = INT_MIN;
            return ret;
        }
        if(hasNext()){
            return Iterator::next();
        }
        throw "Stop iterator!";

            
	}
	
	bool hasNext() const {
	    return peekedNext!= INT_MIN or Iterator::hasNext();
	}
};