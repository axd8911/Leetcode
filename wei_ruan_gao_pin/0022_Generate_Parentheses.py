class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.output = []
        def backtracking(left,right,comb):
            if left == 0 and right == 0:
                self.output.append(comb)
                return
            if left>right or left<0 or right<0:
                return
            backtracking(left-1,right,comb+'(') 
            backtracking(left,right-1,comb+')')
        backtracking(n,n,'')
        return self.output
