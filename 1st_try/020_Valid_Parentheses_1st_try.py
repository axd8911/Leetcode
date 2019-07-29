'''
82%
Use dictionary

Comments:
1. Remove obviously boundaries at the beginning


'''


class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)%2 == 1:
            return False
        match = {'(':')','{':'}','[':']'}
        existing = []
        for item in s:
            if item in match.keys():
                existing.append(item)
            
            if item in match.values():
                if existing == []:
                    return False
                if item != match[existing[-1]]:
                    return False
                else:del existing[-1]
                    
        if existing != []:
            return False

        return True
        
