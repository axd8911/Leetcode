class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)

        for i in range(len(s)):
            if dp[i]:
                for item in wordDict:
                    if s[i:].startswith(item):
                        dp[i+len(item)] = True
        return dp[-1]
