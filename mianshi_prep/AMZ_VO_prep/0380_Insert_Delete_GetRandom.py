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
        self.lis.append(val)
        self.dic[val] = len(self.lis)-1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        if val not in self.dic:
            return False

        position = self.dic[val]
        self.lis[-1],self.lis[position] = self.lis[position],self.lis[-1]
        self.dic[self.lis[position]] = position
        self.lis.pop()

        del self.dic[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not len(self.lis):
            return
        position = random.randrange(0,len(self.lis))
        return self.lis[position]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
