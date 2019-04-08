'''
82%
Think about how you create multiple pareneheses. 
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        count = 0
        combine_start = {'':None}
        combine_end = {'':None}
        while count <= n-1:
            combine_end = {}
            for key in combine_start:
                for j in range(len(key)+1):
                    a = key[:j] + '()' + key[j:]
            
                    if a not in combine_end:
                        combine_end[a] = None
            combine_start = combine_end
            count = count + 1
        
        
        return list(combine_end.keys())
