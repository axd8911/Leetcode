class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.lis = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        self.dic[val] = len(self.lis)
        self.lis.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        valIndex = self.dic[val]
        self.lis[valIndex], self.lis[len(self.lis)-1] = self.lis[len(self.lis)-1],self.lis[valIndex]
        self.dic[self.lis[valIndex]] = valIndex
        self.lis.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.lis[random.randrange(0,len(self.lis))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
