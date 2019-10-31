class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        if len(p) - p.count('*')>len(s):
            return False

        memo = {}

        def helper(i,j):
            if (i,j) not in memo:
                if j == len(p):
                    memo[(i,j)] = i == len(s)
                else:
                    init = i<len(s) and p[j] in {s[i],'?','*'}
                    if p[j] == '*':
                        memo[(i,j)] = init and helper(i+1,j) or helper(i,j+1)
                    else:
                        memo[(i,j)] = init and helper(i+1,j+1)
            return memo[(i,j)]
        return helper(0,0)
                    
