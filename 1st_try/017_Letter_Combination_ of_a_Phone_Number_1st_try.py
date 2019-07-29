'''
72%
A few for loops, O(n**3)
Found that 0 items is often a boundary
'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_dict = {'1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        
        letter_list1 = list(digit_dict[digits[0]])
        
        for i in range(1,len(digits)):
            letter_list2 = []
            for item in letter_list1:
                for letter in digit_dict[digits[i]]:
                    
                    letter_list2.append(item+letter)
                    
            letter_list1 = letter_list2
          
        return letter_list1
        
