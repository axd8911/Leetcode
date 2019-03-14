'''
40%

Convert of numbers and indices:
Should be some better approach to convert numbers faster

Comments:
Return the special and simple conditions as early as possible.
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows < 2:
            return s
        
        rest = len(s)%(2*numRows-2)
        
        makeup = 2*numRows-2-rest
        s = s + ' '*makeup
        counts = int(len(s)/(2*numRows-2))         
        list_convert = ''

        for j in range(numRows):
            for i in range(counts):
                if j == 0:
                    list_convert += (s[i*(2*numRows-2)])
                if numRows > 1 and j == numRows - 1:
                    list_convert += (s[i*(2*numRows-2)+numRows-1])                
            
                if j != 0 and j != numRows - 1:
                    list_convert += (s[i*(2*numRows-2)+j])
                    list_convert += (s[i*(2*numRows-2)+2*numRows-2-j])
        

            
        list_convert = list_convert.replace(' ','')

        return (list_convert)
                
