'''
99.37%

Memory: O(n)
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        output = [1] * (rowIndex+1)
        
        for i in range(1,rowIndex+1):
            for j in range(i-1,0,-1):
                output[j] += output[j-1]
                
        return output
            
