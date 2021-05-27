class Solution:
    def reverse(self, x: int) -> int:
        
        if x<0:
            sign=-1
        else:
            sign=1
        x = abs(x)
        new = 0
        while x:
            new *=10
            new += x%10
            x//=10
        output = new * sign
        if -2**31>output or 2**31-1<output:
            return 0
        return new*sign
            
