'''
99.23%

Of course this question can directly use **, but meaning less.
It is better to follow this rule: 2**25 == 2**16 * 2**8 * 2**1. Rooling the maximum possible number.
'''



class Solution:
    def myPow(self, x: float, n: int) -> float:
        factor = str(bin(n))[::-1]
        
        output = 1
        n = 0
        
        while factor[n] != 'b':
            if factor[n] == '1':
                current = x
                for i in range(n):
                    current = current * current
                output = output * current
            n = n + 1
            print (output, factor[n])
            
        if factor[-1] == '-':
            output = 1/output
            
        return output
