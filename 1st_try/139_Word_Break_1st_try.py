'''
99%
judge the next few letters with consideration of current gap
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #必须是它本身true以及他接下来的几个字符也符合条件
        
        wordDict = {item:None for item in wordDict}
        
        split = [False] * (len(s)+1)
        split[0] = True
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                if split[i] == True and s[i:j+1] in wordDict:
                    split[j+1] = True

        return split[-1]
