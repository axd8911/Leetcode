'''
99%

Reverse the list and do the add one.

'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        
        if digits[0] != 9:
            digits[0] = digits[0] + 1
            return digits[::-1]
        
        n = 0
        while digits[n] == 9:
            digits[n] = 0
            n = n + 1
            if n == len(digits):
                break
        
        if n < len(digits):
            digits[n] = digits[n] + 1
        else:
            digits.append(1)
        return digits[::-1]
