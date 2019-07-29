'''
99.19%
'''


class Solution:
    def __init__(self):
        self.store = {0:1,1:1}
    
    def numTrees(self, n: int) -> int:

        if n in self.store:
            return self.store[n]

        result = 0
        for curr in range(n):
            left = self.numTrees(curr)
            right = self.numTrees(n-curr-1)
            result = result + left * right
        self.store[n] = result

        return result
        
