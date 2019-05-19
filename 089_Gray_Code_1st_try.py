'''
99.76%
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        #0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8
        
        output = [0]
        for i in range(n):
            output += [x + pow(2,i) for x in reversed(output)]
            
        return output
       
        
