'''
67%

Fibonacci Sequence
'''



class Solution:
    def climbStairs(self, n: int) -> int:
 
        a1,a2 = 0,1
        
        for i in range(n+1):
            a = a1 + a2
            a2 = a1
            a1 = a
            
        return a
    
    
