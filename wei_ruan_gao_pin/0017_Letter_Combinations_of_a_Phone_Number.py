class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        curr = collections.deque([''])
        for digit in digits:
            length = len(curr)
            for i in range(length):
                now = curr.popleft()
                for letter in dic[digit]:
                    curr.append(now+letter)
        return curr
                    
                
        
