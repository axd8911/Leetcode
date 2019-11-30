class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        longest = 0
        l,r = 0,0
        cnt = collections.defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]] += 1
            while len(cnt)>k:
                longest = max(longest, r-l)
                cnt[s[l]] -= 1
                if cnt[s[l]] == 0:
                    del cnt[s[l]]
                l += 1

        return max(longest, r-l+1)
