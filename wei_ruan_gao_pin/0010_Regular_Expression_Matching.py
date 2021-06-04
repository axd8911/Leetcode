class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def helper(string, pattern):
            if not pattern:
                return True if not string else False
            init = string!='' and pattern[0] in {string[0],'.'}
            if len(pattern)>1 and pattern[1]=='*':
                return init and helper(string[1:],pattern) or helper(string,pattern[2:])
            else:
                return init and helper(string[1:],pattern[1:])

        return helper(s,p)
