class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        match = {}
        def dp(i,j):
            if (i,j) not in match:
                if j == len(p):
                    match[i,j] = i == len(s)
                else:
                    init_match = i<len(s) and p[j] in {s[i],'.'}
                    if j < len(p)-1 and p[j+1] == '*':
                        match[i,j] = dp(i,j+2) or (init_match and dp(i+1,j))
                    else:
                        match[i,j] = init_match and dp(i+1,j+1)
            return match[i,j]
        return dp(0,0)
 
