'''
99.44%

add the data layer by layer by pop from allData. Important to make the positions clear.

'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        initMat = [[0 for i in range(n)] for j in range(n)]
        allData = [i for i in range(n**2,0,-1)]
        
        cycle = 0
        
        while allData:
            
            for i in range(n-cycle-cycle):
                initMat[cycle][cycle+i] = allData.pop()
            if allData == []: break   
            for i in range(n-cycle-cycle-1):
                initMat[cycle+i+1][-cycle-1] = allData.pop()
            if allData == []: break   
            for i in range(n-cycle-cycle-1):
                initMat[-cycle-1][n-i-cycle-2] = allData.pop()
            if allData == []: break  
            for i in range(n-cycle-cycle-2):
                initMat[n-i-cycle-2][cycle] = allData.pop()
            if allData == []: break  
            cycle = cycle + 1
            
        return initMat
