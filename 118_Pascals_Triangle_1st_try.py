class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        
        output = [[1]]
        cnt = 1
        
        while cnt < numRows:
            cnt = cnt + 1
            output.append([0 for i in range(cnt)])
            output[-1][0] = output[-1][-1] = 1
            for i in range(1,len(output[-1])-1):
                output[-1][i] = output[-2][i-1] + output[-2][i]
            
            
        return output
            
