class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # front to back: once more back than front, remove a back
        # count how many more front, remove them
        countFront = 0
        countBack = 0
        s = list(s)
        result = []
        for i in range(len(s)):
            if s[i] == '(':
                result.append(s[i])
                countFront += 1
            elif s[i] == ')':
                if countBack < countFront:
                    result.append(s[i])
                    countBack += 1
            else:
                result.append(s[i])
        s = result[::-1]
        countFront = 0
        countBack = 0
        result = []
        for i in range(len(s)):
            if s[i] == ')':
                result.append(s[i])
                countFront += 1
            elif s[i] == '(':
                if countBack < countFront:
                    result.append(s[i])
                    countBack += 1
            else:
                result.append(s[i])
        result = result[::-1]
        return ''.join(result)
        
                
