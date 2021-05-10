class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        
        intervals.sort()
        
        for a,b in intervals:
            if not res:
                res.append([a,b])
            else:
                if a<=res[-1][1]:
                    res[-1][1] = max(res[-1][1], b)
                else:
                    res.append([a,b])
        return res
