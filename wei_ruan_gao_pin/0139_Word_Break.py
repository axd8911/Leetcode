class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        good = [True] + [False]*len(s)
        wordDict = set(wordDict)
        for i in range(len(s)):
            if good[i]:
                for j in range(i+1,len(s)+1):
                    if s[i:j] in wordDict:
                        good[j] = good[i] and True
        return good[-1]
    #time:O(N^2)
    #space:O(N)
