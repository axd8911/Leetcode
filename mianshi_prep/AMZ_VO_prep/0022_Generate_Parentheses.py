class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # amount of left and right parentheses

        res = []

        def helper(l,r,curr):
            if l>n or r>l:
                return
            if l==n and r==n:
                res.append(curr)
                return
            helper(l+1,r,curr+'(') or helper(l,r+1,curr+')')


        helper(0,0,'')

        return res
