'''
Leetcode score: 50%
slight redundent, should find a way to simplify the code
run time is (n) with only one layer of for loop.

'''



class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        n = 0
        for i in range(len(S)):
            
            if S[n] == '#':
                if n == 0:
                    S = S[1:]
                    n = n - 1
                else:
                    S = S[:n-1] + S[n+1:]
                    n = n - 2
                    
            if n == len(S):
                break
            
            n = n + 1
                    
        m = 0
        for i in range(len(T)):
            
            if T[m] == '#':
                if m == 0:
                    T = T[1:]
                    m = m - 1
                else:
                    T = T[:m-1] + T[m+1:]
                    m = m - 2
                    
            if m == len(T):
                break
            
            m = m + 1        
        
        
        if S == T: return True
        else: return False
        
