#Hash table
#Time: O(1) to add
#      O(n) to find
#Space: O(n) for the hash map
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.diff = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.diff:
            self.diff[number] = 1
        else:
            self.diff[number]+=1

        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for d in self.diff.keys():
            if value-d in self.diff:
                if d != value-d or self.diff[value-d] >1:
                    return True
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)