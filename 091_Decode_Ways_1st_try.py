'''
99.35%
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '':
            return 0
        
        fact1 = 1
        if s[len(s)-1] == '0':
            fact2 = 0
        else: fact2 = 1
        fact3 = fact2
        
        for i in range(len(s)-2,-1,-1):
            if s[i] == '0':
                fact3 = 0
            
            elif int(s[i]+s[i+1]) > 26:
                fact1 = 0
                fact3 = fact1 + fact2
                
            else:
                fact3 = fact1 + fact2
            
            fact1 = fact2
            fact2 = fact3
            

            
        return fact2
                
                
