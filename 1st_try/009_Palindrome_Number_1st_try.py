'''
45%
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        
        middle = len(x)/2
        if x[int(len(x)/2)::-1] == x[round(len(x)/2+0.4)-1:]: return True
        else: return False
        
