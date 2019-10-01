class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1 or s == s[::-1]:
            return s

        start,longest = 0,1

        for i in range(len(s)):
            strOdd = s[i-longest-1:i+1]
            strEven = s[i-longest:i+1]

            if i - longest - 1 >= 0 and strOdd == strOdd[::-1]:
                start = i - longest - 1
                longest += 2

            elif i - longest >= 0 and strEven == strEven[::-1]:
                start = i - longest
                longest += 1

        return s[start:longest+start]
