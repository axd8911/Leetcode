class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        if len(s)==1:
            return 1

        fact1 = 1

        if s[1] != '0':
            fact2 = fact1
        else:
            fact2 = 0

        if '10' <= s[:2] < '27':
            fact2 += 1
        if len(s)==2:
            return fact2

        for i in range(2,len(s)):
            if '10' <= s[i-1:i+1] < '27':
                fact3 = fact1
            else:
                fact3 = 0
            if s[i]!='0':
                fact3 += fact2
            fact1 = fact2
            fact2 = fact3

        return fact3
