class Solution:
    def modifyString(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if s[i] != '?':
                res += s[i]
            else:
                checker = set()
                if i!=0:
                    checker.add(s[i-1])
                if i!=len(s)-1:
                    checker.add(s[i+1])
                if res:
                    checker.add(res[-1])
                if 'a' not in checker:
                    res += 'a'
                elif 'b' not in checker:
                    res += 'b'
                else:
                    res += 'c'
        return res
