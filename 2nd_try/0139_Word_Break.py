class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        split = [True] + [False] * len(s)
        for i in range(len(s)):
            if split[i]:
                for j in range(i,len(s)):
                    if s[i:j+1] in wordDict:
                        split[j+1] = True
        return split[-1]
