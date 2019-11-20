class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0
        longest = 0
        appear = {}

        for i in range(len(s)):
            if s[i] not in appear:
                appear[s[i]] = i

            else:
                if appear[s[i]] >= start:
                    longest = max(longest,i-start)
                    start = appear[s[i]]+1
                    appear[s[i]] = i


                else:
                    appear[s[i]] = i

        return max(longest, len(s)-start)
