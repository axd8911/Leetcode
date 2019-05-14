'''
99.7%

Sort and go through all items in intervals: extend current range or add new range, depending on edge of output[-1] 

'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if intervals == []:
            return []
        
        intervals.sort()
        output = [intervals[0]]
        
        for i in range(len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1] = [output[-1][0], max(output[-1][1],intervals[i][1])]

            else:
                output.append(intervals[i])
                    
                
        return output
                    
