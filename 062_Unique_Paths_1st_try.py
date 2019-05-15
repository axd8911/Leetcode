'''
99.91%

Although mathmatic approach achieves very fast running, it is still important to review the recursion and iteration ways.
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        steps = 1
        for i in range(m,m+n-1):
            steps = steps * i
            
        repeat = 1
        for i in range(1,n):
            repeat = repeat * i
            
        return int(steps/repeat)
        
        
