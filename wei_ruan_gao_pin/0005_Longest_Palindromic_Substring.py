class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        length = 0
        for i in range(len(s)):
            str1 = s[i-length-1:i+1]
            str2 = s[i-length:i+1]
            if i-length-1 >=0 and str1 == str1[::-1]:
                start = i-length-1
                length+= 2
            elif i-length >= 0 and str2 == str2[::-1]:
                start = i-length
                length += 1
        return s[start:start+length]
