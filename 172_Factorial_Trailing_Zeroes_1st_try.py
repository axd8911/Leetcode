'''
98.5%
'''

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        cnt = 0
        divider = 5
        expon = 1
        
        while n >= (divider**expon):
            
            cnt += n // (divider**expon)
            expon = expon + 1
        
        return cnt
