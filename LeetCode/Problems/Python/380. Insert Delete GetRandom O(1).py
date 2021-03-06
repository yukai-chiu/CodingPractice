class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}
        self.data = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.lookup:
            return False
        self.data.append(val)
        self.lookup[val] = len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.lookup or not self.data:
            return False
        #swap to end
        self.lookup[self.data[-1]] = self.lookup[val]
        self.data[self.lookup[val]], self.data[-1] = self.data[-1], self.data[self.lookup[val]]
        del self.lookup[val]
        self.data.pop()
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.data[random.randint(0, len(self.data)-1)]

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        self.lookup = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data:
            self.data[val] = len(self.lookup)
            self.lookup.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.data:
            last = self.lookup[-1]
            self.lookup[self.data[val]], self.lookup[-1] = self.lookup[-1], self.lookup[self.data[val]]
            self.data[last], self.data[val] = self.data[val], self.data[last]
            
            self.lookup.pop()
            del self.data[val]
    
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        r = random.randint(0,len(self.lookup)-1)
        return self.lookup[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()