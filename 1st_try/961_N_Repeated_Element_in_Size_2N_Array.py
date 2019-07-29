'''
99.65%


'''



class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        
        n = 0
        
        for item in A:
            if item not in A[:n]:
                n = n+1
            else: return item
        
        
