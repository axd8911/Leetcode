'''
99.94%

A fact of Math problem. Recursion and iteration could be used but much slower.
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        output = []
        factor = 1
        k=k-1
        allData = [str(i) for i in range(1,n+1)]
        for i in range(1,n):
            factor = factor * i
        
        while k != 0:
            n = n - 1
            output.append(allData.pop(int(k//factor)))
            k = k%factor
            factor = factor / n
            
        output = output + allData
        return ''.join(output)
            
            
