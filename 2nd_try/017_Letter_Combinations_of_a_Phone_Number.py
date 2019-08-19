class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        match = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        output = []
        length = len(digits)

        def bt(comb,idx):
            #print (1,comb)
            if len(comb) == length:
                output.append(comb)
                return

            for i in range(len(match[digits[idx]])):
                bt(comb+match[digits[idx]][i],idx+1)

        if digits:
            bt('',0)
        return output
        
