'''
Easy question
97%
One for loop. May still try to simplify the code in for loop.
'''



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
                
        if len(strs) == 0:
            return ''
        
        temp_long = strs[0]
        for i in range(len(strs)):
            
            if len(strs[i]) < len(temp_long):
                temp_long = temp_long[:len(strs[i])]
            while temp_long != strs[i][:len(temp_long)]:
                temp_long = temp_long[:len(temp_long)-1]
                     
        return temp_long
            


                    
                
                
