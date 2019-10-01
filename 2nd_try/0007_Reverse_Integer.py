class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            negative = True
            x *= (-1)
        else:
            negative = False
        new = 0
        while x:
            res = x%10
            new = new*10+res
            x//=10
        if new>2**31-1 or new<-2**31:
            return 0
        if negative:
            return new*(-1)
        return new
