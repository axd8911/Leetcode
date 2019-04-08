'''
Not a successful one. Should come back and try again. This is just a place holder in case I forget that.
'''



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend/divisor < -2**31 or dividend/divisor >2**31-1:
            return 2**31-1
        
        
        if dividend*divisor >= 0:
            return dividend//divisor
    
        else:
            return int(dividend/divisor)
