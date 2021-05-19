class Solution:
    def numDecodings(self, s: str) -> int:
        cnt = [1]
        for i in range(len(s)):
            factor1, factor2 = 0,0
            if i == 0:
                if s[i] =='0':
                    return 0
                else:
                    cnt.append(1)
            else:
                if s[i] != '0':
                    factor1 = cnt[-1]
                if '10'<=s[i-1:i+1]<='26':
                    factor2 = cnt[-2]
                cnt.append(factor1+factor2)
        return cnt [-1]
