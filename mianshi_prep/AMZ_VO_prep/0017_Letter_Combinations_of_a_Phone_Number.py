class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        res = ['']

        for digit in digits:
            newRes = []
            for letter in dic[digit]:
                newRes += [item+letter for item in res]
            res = newRes

        return res


# recursion
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        length = len(digits)
        res = []

        def helper(combine,idx):
            if len(combine) == length:
                res.append(combine)
                return

            for i in range(idx,len(digits)):
                for letter in dic[digits[i]]:
                    helper(combine+letter,i+1)

        helper('',0)
        return res
