class Solution:
    def isValid(self, s: str) -> bool:
        match = {'(':')','[':']','{':'}'}
        front = '({['
        back = ')}]'
        
        stack = []
        
        for item in s:
            if item in front:
                stack.append(item)
            else:
                if not stack or match[stack[-1]] != item:
                    return False
                stack.pop()
        if stack:
            return False
        return True
            
